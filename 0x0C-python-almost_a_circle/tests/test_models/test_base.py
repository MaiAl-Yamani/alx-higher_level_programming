#!/usr/bin/python3
"""
Unittests for Base Class
"""

from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import unittest, json


class TestBaseClass(unittest.TestCase):
    """Test for Base class."""
    
    @classmethod
    def setUpClass(cls):
        """setup class method"""
        cls.bs1 = Base()
        cls.bs2 = Base(50)
        cls.bs3 = Base()
        cls.rt1 = Rectangle(5, 5)
        cls.rt2 = Rectangle(20, 20, id=1000)
        cls.rt3 = Rectangle(30, 30, 3, 3, id=100)
        cls.sq1 = Square(10)
        cls.sq2 = Square(5, 5, 4, id=200)
        cls.sq3 = Square(12, id=22)

    @classmethod
    def tearDownClass(cls):
        """delete objects after tests."""
        del cls.bs1
        del cls.bs2
        del cls.bs3

    def test_base_cls_doc(self):
        """tests docstring for base class."""
        self.assertIsNotNone(Base.__doc__)

    def test_base_instance_doc(self):
        """checks if base class instance is present."""
        self.assertIsNotNone(self.bs1.__doc__)
        self.assertIsNotNone(self.rt1.__doc__)
        self.assertIsNotNone(self.sq1.__doc__)

    def test_base_methods_doc(self):
        """checks docstring for all methods."""
        self.assertTrue(Base.__init__.__doc__)
        self.assertTrue(Base.save_to_file_csv.__doc__)
        self.assertTrue(Base.load_from_file_csv.__doc__)
        self.assertTrue(Base.to_json_string.__doc__)
        self.assertTrue(Base.from_json_string.__doc__)
        self.assertTrue(Base.save_to_file.__doc__)
        self.assertTrue(Base.create.__doc__)
        self.assertTrue(Base.load_from_file.__doc__)

    def test_class_attr_exist(self):
        """checks if class attribute exists."""
        self.assertIsNotNone(Base._Base__nb_objects)

    def test_base_init_id(self):
        """base instantiation check."""
        self.assertEqual(self.bs1.id, 1)
        self.assertEqual(self.bs2.id, 50)
        self.assertEqual(self.bs3.id, 2)

    def test_obj_id_exist(self):
        """check id for objects."""
        self.assertIsNotNone(self.bs1.id)
        self.assertIsNotNone(Base._Base__nb_objects)

    def test_cls_attr_match_id(self):
        """check if id matches class attr."""
        self.assertEqual(Base._Base__nb_objects, self.sq1.id)

    def test_obj_id(self):
        """checks object id is correct."""
        self.assertEqual(self.rt2.id, 1000)
        self.assertEqual(self.sq2.id, 200)
        self.assertEqual(self.sq3.id, 22)
        self.assertEqual(self.bs1.id, 1)

    def test_base_methods(self):
        """chicks if method exists for base class."""
        self.assertTrue(hasattr(Base, "__init__"))
        self.assertTrue(hasattr(Rectangle, "integer_validator"))
        self.assertTrue(hasattr(Base, "save_to_file_csv"))
        self.assertTrue(hasattr(Base, "load_from_file_csv"))
        self.assertTrue(hasattr(Base, "to_json_string"))
        self.assertTrue(hasattr(Base, "from_json_string"))
        self.assertTrue(hasattr(Base, "save_to_file"))
        self.assertTrue(hasattr(Base, "create"))
        self.assertTrue(hasattr(Base, "load_from_file"))

    def test_int_value(self):
        """value error check"""
        with self.assertRaises(ValueError):
            self.rt1.integer_validator(-20, -20)

    def test_int_type(self):
        """type error check"""
        with self.assertRaises(TypeError):
            self.rt2.integer_validator2("str", "str")

    def test_to_json(self):
        """test to and from json methods"""
        list1 = [
            {'id': 100},
            {'height': 88},
            {'width': 1, 'id': 2, 'height': 88},
            {'id': 4, 'height': 144, 'weight': 700},
            {'width': 22, 'height': 11}
            ]
        empty = []

        rect_to_json = Rectangle.to_json_string(list1)
        base_to_json = Base.to_json_string(list1)

        rect_to_empty_json = Rectangle.to_json_string(empty)
        base_to_empty_json = Base.to_json_string(empty)

        self.assertIsInstance(list1, list)
        self.assertIsInstance(rect_to_json, str)
        self.assertIsInstance(base_to_json, str)

        self.assertIsInstance(empty, list)
        self.assertIsInstance(rect_to_empty_json, str)
        self.assertIsInstance(base_to_empty_json, str)

        rect_from_json = Rectangle.from_json_string(rect_to_json)
        base_from_json = Base.from_json_string(rect_to_json)
        
        self.assertIsInstance(rect_from_json, list)
        self.assertIsInstance(base_from_json, list)

    def test_create(self):
        """test create method"""
        self.assertIsNotNone(self.sq2.__init__)
        self.assertIsNotNone(self.rt2.__dict__)

        attrs = ["width", "height", "x", "y", "id"]
        for attr in attrs:
            self.assertTrue(hasattr(self.rt2, attr))

        rt_dict = self.rt3.to_dictionary()
        rt_create = Rectangle.create(**rt_dict)
        self.assertEqual(self.rt3.__str__(), '[Rectangle] (100) 3/3 - 30/30')


if __name__ == '__main__':
        unittest.main()
