import unittest
from models.square import Square
from models.base import Base
import os


class TestSquare(unittest.TestCase):
    def test_init(self):
        """Initialization of a Test Square class"""
        # Test default initialization
        square = Square(5)
        self.assertEqual(square.id, None)
        self.assertEqual(square.size, 5)
        self.assertEqual(square.x, 0)
        self.assertEqual(square.y, 0)

        # Test custom initialization
        square = Square(10, 2, 3, 1)
        self.assertEqual(square.id, 1)
        self.assertEqual(square.size, 10)
        self.assertEqual(square.x, 2)
        self.assertEqual(square.y, 3)

    def test_str(self):
        """Test Square class string representation"""
        square = Square(5, 2, 3, 1)
        self.assertEqual(str(square), "[Square] (1) 2/3 - 5")

    def test_size_property(self):
        """Test Square size property and size setter"""
        square = Square(5)
        self.assertEqual(square.size, 5)

        square.size = 10
        self.assertEqual(square.size, 10)
        self.assertEqual(square.width, 10)
        self.assertEqual(square.height, 10)

    def test_update(self):
        """Test Square class update method"""
        square = Square(5, 2, 3, 1)
        square.update(2, 10, 4, 5)
        self.assertEqual(square.id, 2)
        self.assertEqual(square.size, 10)
        self.assertEqual(square.x, 4)
        self.assertEqual(square.y, 5)

        square.update(size=20)
        self.assertEqual(square.size, 20)

        square.update(3)
        self.assertEqual(square.id, 3)

        square.update(y=8, x=6, size=15, id=4)
        self.assertEqual(square.id, 4)
        self.assertEqual(square.size, 15)
        self.assertEqual(square.x, 6)
        self.assertEqual(square.y, 8)

    def test_to_dictionary(self):
        """Test Square class to_dictionary method"""
        square = Square(5, 2, 3, 1)
        square_dict = square.to_dictionary()

        self.assertEqual(square_dict, {'id': 1, 'size': 5, 'x': 2, 'y': 3})

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
