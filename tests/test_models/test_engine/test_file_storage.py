#!/usr/bin/python3
"""Test Module that contain the test of class amenity"""


import unittest
from models.engine.file_storage import FileStorage
from models import storage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    """test class Amenity"""

    def setUp(self):
        """create a instance"""
        self.new_file_storage = FileStorage()

    def test_function_all(self):
        """ this function should return the dictionary __objects
        """
        setattr(FileStorage, "_FileStorage__objects", {})

        instance = FileStorage()
        self.assertEqual(instance.all(), {})

        setattr(FileStorage, "_FileStorage__objects", {"Hola", "Mundo"})
        self.assertEqual(instance.all(), {"Hola", "Mundo"})
        setattr(FileStorage, "_FileStorage__objects", {})


if __name__ == "__main__":
    unittest.main()
