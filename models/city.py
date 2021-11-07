#!/usr/bin/python3
"""Module that defines all common attributes/methods for other classes """
from models import State
from models.base_model import BaseModel


class City(BaseModel):
    """Class that represents model of state"""
    state_id = ""
    name = ""
