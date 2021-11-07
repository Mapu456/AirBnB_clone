#!/usr/bin/python3
"""Test Module that contain the test of class amenity"""


import unittest
from models.place import Place


class TestPlace(unittest.TestCase):
    """Test Place"""

    def setUp(self):
        """create a instance"""
        self.new_place = Place()

    def test_place(self):
        """check the type attributes"""
        self.assertEqual(type(self.new_place.name), str)
        self.assertEqual(type(self.new_place.number_bathrooms), int)
        self.assertEqual(type(self.new_place.price_by_night), int)
        self.assertEqual(type(self.new_place.max_guest), int)
        self.assertEqual(type(self.new_place.number_rooms), int)
        self.assertEqual(type(self.new_place.latitude), float)
        self.assertEqual(type(self.new_place.longitude), float)
        self.assertEqual(type(self.new_place.description), str)
        self.assertEqual(type(self.new_place.amenity_ids), list)
        self.assertEqual(type(self.new_place.city_id), str)
        self.assertEqual(type(self.new_place.user_id), str)
