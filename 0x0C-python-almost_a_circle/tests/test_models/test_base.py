#!/usr/bin/python3
"""the unittest for base.py"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
import os
import json


class Test_Base(unittest.TestCase):
    """Definition of class to evaluate test cases for base.py"""

    def test_with_id(self):
        """Evaluating instance of the class"""
        z1 = Base()
        self.assertIsInstance(z1, Base)
        self.assertFalse(type(z1) == type(Base))
        self.assertFalse(id(z1) == id(Base))
        z2 = Base()
        self.assertTrue(type(z1) == type(z2))
        self.assertFalse(id(z1) == id(z2))

    def test_with_none_id(self):
        """Evaluating when id is none"""
        z1 = Base(id=1)
        self.assertEqual(z1.id, 1)
        z1 = Base(id=3)
        self.assertEqual(z1.id, 3)

    def test_with_none_id_increment(self):
        """Evaluating if id increment correctly"""
        z1 = Base()
        z2 = Base()
        self.assertEqual(z2.id, 2)

    def test_id_value(self):
        """evaluating value of id"""
        z1 = Base(50)
        self.assertEqual(z1.id, 50)
        z1 = Base(-7)
        self.assertEqual(z1.id, -7)
        z1 = Base(0)
        self.assertEqual(z1.id, 0)
        z1 = Base(1000e+1000)
        self.assertEqual(z1.id, 1000e+1000)
        z1.__init__(4)
        self.assertEqual(z1.id, 4)
:
    def test_obj_attributes(self):
        """evaluating objects attributes"""
        z1 = Base()
        self.assertEqual(z1.__dict__, {'id': 1})
        z2 = Base(90)
        self.assertEqual(z2.__dict__, {'id': 90})

    def test_json_string(self):
        """evaluating for json string method"""
        f1 = Rectangle(10, 7, 2, 8, 30)
        dict_f1 = f1.to_dictionary()
        json_dict_f1 = Base.to_json_string([dict_f1])
        self.assertEqual(json.loads(json_dict_f1), [dict_f1])

        f1 = Rectangle(50, 40)
        dict_f2 = f1.to_dictionary()
        json_dict_f2 = Base.to_json_string([dict_f2])
        self.assertEqual(json.loads(json_dict_f2), [dict_f2])

        empty_dict = {}
        json_empty_dict = Base.to_json_string([empty_dict])
        self.assertEqual(json.loads(json_empty_dict), [empty_dict])

    def tearDown(self):
        """Tear down test method to reset class attribute
        """
        Base._Base__nb_objects = 0
        try:
            os.remove("Rectangle.json")
        except Exception:
            pass
        try:
            os.remove("Square.json")
        except Exception:
            pass
        try:
            os.remove("Rectangle.csv")
        except Exception:
            pass
        try:
            os.remove("Square.csv")
        except Exception:
            pass


if __name__ == '__main__':
    unittest.main()
