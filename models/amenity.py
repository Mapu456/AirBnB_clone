#!/usr/bin/python3
"""Module that defines all common attributes/methods for other classes """
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Class that represents model of Amenity"""
    name = ""
