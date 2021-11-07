#!/usr/bin/python3
"""Module that defines all common attributes/methods for other classes """
from models.base_model import BaseModel
from models.place import Place
from models.user import User


class Review(BaseModel):
    """Class that represents model of Review"""
    place_id = ""
    user_id = ""
    text = ""
