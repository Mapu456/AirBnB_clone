#!/usr/bin/python3
"""Module that defines all common attributes/methods for other classes """
import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """Class tha represents model of BaseModel"""

    def __init__(self, *args, **kwargs):
        """Constructor method for the BaseModel"""
        if len(kwargs) == 0:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)
        else:
            self.id = kwargs.get("id")
            self.created_at = datetime.strptime(
                kwargs.get("created_at"), "%Y-%m-%dT%H:%M:%S.%f")
            self.updated_at = datetime.strptime(
                kwargs.get("updated_at"), "%Y-%m-%dT%H:%M:%S.%f")

    def __str__(self):
        """
        str [<class name>] (<self.id>) <self.__dict__>
        """
        msg = "[{}] ({}) {}"
        return msg.format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """
        Public instance method that  updates the public instance
        attribute updated_at with the current datetime
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        Public instance method that returns a dictionary containing
        all keys/values of __dict__ of the instance.
        """
        new_dict = {}
        new_dict = self.__dict__.copy()
        new_dict["__class__"] = self.__class__.__name__
        new_dict["created_at"] = datetime.isoformat(self.created_at)
        new_dict["updated_at"] = datetime.isoformat(self.updated_at)
        return (new_dict)