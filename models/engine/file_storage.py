#!/usr/bin/python3
"""Module that serializes/deserializes JSON file to instances"""
import json


class FileStorage:
    """
    Class FileStorage that serializes instances to a JSON file
    and deserializes JSON file to instances
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Public instance method that returns the dictionary __objects
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        Sets in __objects the obj with key <obj class name>.id
        """
        object_key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[object_key] = obj

    def save(self):
        """
        serializes __objects to the JSON file (path: __file_path)
        """
        new_dict = {}
        for key, value in self.all().items():
            new_dict[key] = value.to_dict().copy()
        with open(FileStorage.__file_path, 'w', encoding='UTF8') as f:
            data = json.dumps(new_dict)
            f.write(data)

    def reload(self):
        from models.base_model import BaseModel
        new_dict = {}
        try:
            with open(FileStorage.__file_path, 'r', encoding='UTF8') as f:
                new_dict = json.load(f)
                for key, value in new_dict.items():
                    class_name = value.get('__class__')
                    obj = eval(class_name + '(**value)')
                    self.all()[key] = obj
        except FileNotFoundError as e:
            pass
