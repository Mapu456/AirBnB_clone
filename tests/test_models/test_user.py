#!/usr/bin/python3
"""Test Module that contain the test of class User"""

import unittest
from models.user import User


class TestUser(unittest.TestCase):
    """Test class User"""

    def setUp(self):
        """create a instance"""
        self.new_user = User()

    def test_user(self):
        """check the type attributes"""
        self.assertEqual(type(self.new_user.email), str)
        self.assertEqual(type(self.new_user.first_name), str)
        self.assertEqual(type(self.new_user.password), str)
        self.assertEqual(type(self.new_user.last_name), str)
