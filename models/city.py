#!/usr/bin/python3
"""Module that defines all common attributes/methods for other classes """
from models import state
from models.base_model import BaseModel
from models.state import State

class City(BaseModel):
    """Class that represents model of state"""
    if State.id is not None:
        state_id = State.id
    else:
        state_id = ""
    name = ""
