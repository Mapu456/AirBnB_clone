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
            self.created_at = datetime.strptime(kwargs.get("created_at"), "%Y-%m-%dT%H:%M:%S.%f")
            self.updated_at = datetime.strptime(kwargs.get("updated_at"), "%Y-%m-%dT%H:%M:%S.%f")

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
        storage.save(self)

    def to_dict(self):
        """
        Public instance method that returns a dictionary containing
        all keys/values of __dict__ of the instance.
        """
        self.__dict__["__class__"] = self.__class__.__name__
        self.__dict__["created_at"] = datetime.isoformat(self.created_at)
        self.__dict__["updated_at"] = datetime.isoformat(self.updated_at)
        return (self.__dict__)



if __name__ == "__main__":
    import time
    my_model = BaseModel()
    my_model.name = "My_First_Model"
    my_model.my_number = 89
    print(my_model.id)
    print(my_model)
    print(type(my_model.created_at))
    print("--")
    my_model_json = my_model.to_dict()
    print(my_model_json)
    print("JSON of my_model:")
    for key in my_model_json.keys():
        print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))
        
    print("--")
    my_new_model = BaseModel(**my_model_json)
    print(my_new_model.id)
    print(my_new_model)
    print(type(my_new_model.created_at))

print("--")
print(my_model is my_new_model)
