#!/usr/bin/python3
"""Unittest for rectangle.py file
"""
import unittest
import os
from models.base import Base
from models.rectangle import Rectangle
from unittest.mock import patch
from io import StringIO


class Test_rectangle(unittest.TestCase):
    """Definition of  a class to evaluate diferent test cases for rectangle.py file
    """

    def test_instance_class(self):
        """Evaluate for a instance of the class
        """
        f1 = Rectangle(10, 2)
        self.assertIsInstance(f1, Rectangle)
        self.assertTrue(issubclass(Rectangle, Base))
        self.assertTrue(id(Rectangle) != id(Base))
        self.assertTrue(type(Rectangle) == type(Base))
        f2 = Rectangle(2, 5)
        self.assertTrue(type(f1) == type(f2))
        self.assertFalse(id(f1) == id(f2))

    def test_init_attributes(self):
        """Evaluate when id is none
        """
        f1 = Rectangle(10, 60)
        self.assertEqual(f1.id, 1)
        self.assertEqual(f1.width, 10)
        self.assertEqual(f1.height, 60)
        self.assertEqual(f1.x, 0)
        self.assertEqual(f1.y, 0)

        f2 = Rectangle(20, 40)
        self.assertEqual(f2.id, 2)
        self.assertEqual(f2.width, 20)
        self.assertEqual(f2.height, 40)
        self.assertEqual(f2.x, 0)
        self.assertEqual(f2.y, 0)

        f3 = Rectangle(10, 2, 4, 5)
        self.assertEqual(f3.id, 3)
        self.assertEqual(f3.width, 10)
        self.assertEqual(f3.height, 2)
        self.assertEqual(f3.x, 4)
        self.assertEqual(f3.y, 5)

        f4 = Rectangle(10, 2, 6)
        self.assertEqual(f4.id, 4)
        self.assertEqual(f4.width, 10)
        self.assertEqual(f4.height, 2)
        self.assertEqual(f4.x, 6)
        self.assertEqual(f4.y, 0)

        f5 = Rectangle(10, 2, 4, 5, 50)
        self.assertEqual(f5.id, 50)
        self.assertEqual(f5.width, 10)
        self.assertEqual(f5.height, 2)
        self.assertEqual(f5.x, 4)
        self.assertEqual(f5.y, 5)

        f6 = Rectangle(10, 2, 4, 5, 180)
        f6.id = 50
        self.assertEqual(f6.id, 50)
        f6.width = 100
        self.assertEqual(f6.width, 100)
        f6.height = 200
        self.assertEqual(f6.height, 200)
        f6.x = 40
        self.assertEqual(f6.x, 40)
        f6.y = 50
        self.assertEqual(f6.y, 50)

    def test_raise_errors(self):
        """Check for raises errors
        """
        # Evaluate for diferents instances
        with self.assertRaises(TypeError):
            f1 = Rectangle()
        with self.assertRaises(NameError):
            f1 = Rectangle_shape()
        with self.assertRaises(AttributeError):
            f1 = Rectangle(10, 80)
            f1.to_json()
        with self.assertRaises(TypeError):
            f2 = Rectangle(10)
        with self.assertRaises(ValueError):
            f3 = Rectangle(10, -4)
        with self.assertRaises(ValueError):
            f4 = Rectangle(-10, 4)
        with self.assertRaises(TypeError):
            f5 = Rectangle(10, "4")
        with self.assertRaises(TypeError):
            f6 = Rectangle("10", 4)
        with self.assertRaises(TypeError):
            f7 = Rectangle(10, 4, "9")
        with self.assertRaises(TypeError):
            f8 = Rectangle(10, 4, 9, "20")
        with self.assertRaises(ValueError):
            f9 = Rectangle(10, 4, -5, 7)
        with self.assertRaises(ValueError):
            f10 = Rectangle(10, 4, 5, -10)
        with self.assertRaises(TypeError):
            f11 = Rectangle(10, 4, 5, 10, 30, 60)
        with self.assertRaises(ValueError):
            f12 = Rectangle(0, 10)
        with self.assertRaises(ValueError):
            f13 = Rectangle(15, 0)

        # Evaluate for setters
        with self.assertRaises(TypeError):
            f1.x = "4"
        with self.assertRaises(ValueError):
            f1.x = -4
        with self.assertRaises(ValueError):
            f1.width = -10
        with self.assertRaises(TypeError):
            f1.width = "10"
        with self.assertRaises(TypeError):
            f1.height = "30"
        with self.assertRaises(ValueError):
            f1.height = -10
        with self.assertRaises(TypeError):
            f1.y = "10"
        with self.assertRaises(ValueError):
            f1.y = -10
        # Evaluate for update method
        with self.assertRaises(ValueError):
            f1.update(10, -10, 20, 40)
        with self.assertRaises(TypeError):
            f1.update(10, 10, "20", 40)
        with self.assertRaises(ValueError):
            f1.update(id=10, x=10, y=20, width=40, height=-60)
        with self.assertRaises(TypeError):
            f1.update(id=10, x=10, y=20, width="30", height=40)
        with self.assertRaises(AttributeError):
            f2 = None
            f2.to_dictionary

    def test_area(self):
        """Check area method of rectangle objects
        """
        f1 = Rectangle(3, 2)
        area = f1.area()
        self.assertEqual(area, 6)

        f2 = Rectangle(3, 2)
        area = Rectangle.area(f2)
        self.assertEqual(area, 6)

        f3 = Rectangle(30, 20, 4, 5, 10)
        area = f3.area()
        self.assertEqual(area, 600)

        f4 = Rectangle(5, 5, 4)
        area = f4.area()
        self.assertEqual(area, 25)

    def test_display(self):
        """Evaluate display method
        """
        output_1 = "#\n"
        f1 = Rectangle(1, 1)
        with patch('sys.stdout', new=StringIO()) as mock_out:
            f1.display()
            self.assertEqual(mock_out.getvalue(), output_1)

        output_2 = "#####\n#####\n"
        f2 = Rectangle(5, 2)
        with patch('sys.stdout', new=StringIO()) as mock_out:
            f2.display()
            self.assertEqual(mock_out.getvalue(), output_2)

        output_3 = "\n\n##\n##\n"
        f3 = Rectangle(2, 2, 0, 2)
        with patch('sys.stdout', new=StringIO()) as mock_out:
            f3.display()
            self.assertEqual(mock_out.getvalue(), output_3)

        output_4 = "  ##\n  ##\n"
        f4 = Rectangle(2, 2, 2, 0)
        with patch('sys.stdout', new=StringIO()) as mock_out:
            f4.display()
            self.assertEqual(mock_out.getvalue(), output_4)

        output_5 = "\n\n  ##\n  ##\n"
        f5 = Rectangle(2, 2, 2, 2)
        with patch('sys.stdout', new=StringIO()) as mock_out:
            f5.display()
            self.assertEqual(mock_out.getvalue(), output_5)

    def test_str(self):
        """Evaluate str method
        """
        f1 = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(f1), "[Rectangle] (12) 2/1 - 4/6")
        f2 = Rectangle(5, 5, 1)
        self.assertEqual(str(f2), "[Rectangle] (1) 1/0 - 5/5")
        f3 = Rectangle(5, 5)
        self.assertEqual(str(f3), "[Rectangle] (2) 0/0 - 5/5")
        f4 = Rectangle(4, 6, 2, 1, 50)
        self.assertEqual(f4.__str__(), "[Rectangle] (50) 2/1 - 4/6")

    def test_update(self):
        """Evaluate update method
        """
        f1 = Rectangle(10, 10, 10, 10)
        self.assertEqual(f1.__str__(), "[Rectangle] (1) 10/10 - 10/10")
        f1.update(height=1)
        self.assertEqual(f1.__str__(), "[Rectangle] (1) 10/10 - 10/1")
        f1.update(width=1, x=2)
        self.assertEqual(f1.__str__(), "[Rectangle] (1) 2/10 - 1/1")
        f1.update(y=1, width=2, x=3, id=89)
        self.assertEqual(f1.__str__(), "[Rectangle] (89) 3/1 - 2/1")
        f1.update(x=1, height=2, y=3, width=4)
        self.assertEqual(f1.__str__(), "[Rectangle] (89) 1/3 - 4/2")
        f1.update(x=1, height=2, y=3, width=4, id=30)
        self.assertEqual(f1.__str__(), "[Rectangle] (30) 1/3 - 4/2")
        f1.update(id=67)
        self.assertEqual(f1.__str__(), "[Rectangle] (67) 1/3 - 4/2")
        f1.update(10, 10, 10, 10, 10, x=1, height=2, y=3, width=4, id=30)
        self.assertEqual(f1.__str__(), "[Rectangle] (10) 10/10 - 10/10")
        f1.update(45, x=1, height=2, y=3, width=4, id=30)
        self.assertEqual(f1.__str__(), "[Rectangle] (45) 10/10 - 10/10")
        f1.update(73, id=30)
        self.assertEqual(f1.__str__(), "[Rectangle] (73) 10/10 - 10/10")
        f1.update(50)
        self.assertEqual(f1.__str__(), "[Rectangle] (50) 10/10 - 10/10")
        f1.update()
        self.assertEqual(f1.__str__(), "[Rectangle] (50) 10/10 - 10/10")

    def test_dictionary_representation(self):
        """Evaluate to_dictionary method
        """
        f1 = Rectangle(10, 2, 1, 9)
        f1_dictionary = r1.to_dictionary()
        self.assertEqual(f1_dictionary, {'x': 1, 'y': 9, 'id': 1, 'height': 2,
                                         'width': 10})

        f2 = Rectangle(10, 2, 1, 9, 30)
        f2_dictionary = r2.to_dictionary()
        self.assertEqual(f2_dictionary, {'x': 1, 'y': 9, 'id': 30, 'height': 2,
                                         'width': 10})

        f3 = Rectangle(10, 2)
        f3_dictionary = r3.to_dictionary()
        self.assertEqual(f3_dictionary, {'x': 0, 'y': 0, 'id': 2, 'height': 2,
                                         'width': 10})

        f4 = Rectangle(10, 2)
        f4_dictionary = r4.to_dictionary()
        self.assertEqual(f4_dictionary, {'x': 0, 'y': 0, 'id': 3, 'height': 2,
                                         'width': 10})

        f5 = Rectangle(10, 2, 5, 6)
        f5_dictionary = r5.to_dictionary()
        self.assertEqual(f5_dictionary, {'x': 5, 'y': 6, 'id': 4, 'height': 2,
                                         'width': 10})

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
