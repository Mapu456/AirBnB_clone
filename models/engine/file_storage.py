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
        print(object_key)
        FileStorage.__objects[object_key] = obj

    def save(self):
        """
        serializes __objects to the JSON file (path: __file_path)
        """
        with open(FileStorage.__file_path, 'w', encoding='UTF8') as f:
            json.dump(__objects, f)
        
