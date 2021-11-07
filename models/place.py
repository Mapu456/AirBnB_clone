#!/usr/bin/python3
"""Module that defines all common attributes/methods for other classes """
from models import city
from models import user
from models.base_model import BaseModel
from models.city import City
from models.user import User

class Place(BaseModel):
    """Class that represents model of Place"""
    if City.id is not None:
        city_id = City.id
    else:
        city_id = ""
    if User.id is not None:
        user_id = User.id
    else:
        user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
