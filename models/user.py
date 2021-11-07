#!/usr/bin/python3
"""Module that defines all common attributes/methods for other classes """
from models.base_model import BaseModel


class User(BaseModel):
    """Class that represents model of user"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
