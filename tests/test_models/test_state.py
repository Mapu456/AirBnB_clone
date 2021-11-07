#!/usr/bin/python3
"""Test Module that contain the test of class state"""

import unittest
from models.state import State


class TestState(unittest.TestCase):
    """Test class state"""

    def setUp(self):
        """create a instance"""
        self.new_state = State()

    def test_state(self):
        """check the type attributes"""
        self.assertEqual(type(self.new_state.name), str)
