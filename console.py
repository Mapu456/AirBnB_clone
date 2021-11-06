#!/usr/bin/python3
"""Module that defines all common attributes/methods for other classes """

import cmd
import json
import sys
from models import base_model
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """
    Class that contains the entry point of the command interpreter
    """
    class_list = ['BaseModel', 'User', 'State',
                  'City', 'Amenity', 'Place', 'Review']
    prompt = '(hbnb) '

    def do_quit(self, arg):
        'Quit command to exit the program'
        return True

    def do_EOF(self, arg):
        'EOF command to exit the program'
        return True

    def emptyline(self):
        pass

    def do_create(self, arg):
        ' Creates a new instance of BaseModel, saves it and prints the id'
        if arg == "":
            print("** class name missing **")
        elif arg in HBNBCommand.class_list:
            instance_class = ("{}()".format(arg))
            p = eval(instance_class)
            p.save()
            print(p.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, arg):
        'Prints the string of an instance based on the class name and id'
        arguments = arg.split(" ")
        if arguments[0] == "":
            print("** class name missing **")
        elif arguments[0] in HBNBCommand.class_list:
            class_string = arguments[0]
            if arguments[0] == class_string and len(arguments) == 1:
                print("** instance id missing **")
            else:
                if arguments[0] == class_string and len(arguments[1]) != 0:
                    all_objects = storage.all()
                    switch = 0
                    for obj_id in all_objects.keys():
                        obj = all_objects[obj_id]
                        if obj.id == arguments[1]:
                            print(obj)
                            switch = 1
                    if switch == 0:
                        print("** no instance found **")
        else:
            print("** class doesn't exist **")

    def do_destroy(self, arg):
        'Deletes an instance based on the class name and id (save JSON file)'
        arguments = arg.split(" ")
        if arguments[0] == "":
            print("** class name missing **")
        elif arguments[0] in HBNBCommand.class_list:
            class_string = arguments[0]
            if arguments[0] == class_string and len(arguments) == 1:
                print("** instance id missing **")
            else:
                if arguments[0] == class_string and len(arguments[1]) != 0:
                    all_objects = storage.all()
                    try:
                        del all_objects["{}.{}".format(
                            arguments[0], arguments[1])]
                        storage.save()
                    except KeyError as e:
                        print("** no instance found **")
        else:
            print("** class doesn't exist **")

    def do_all(self, arg):
        'Prints all string of all instances based or not on the class name'
        objs_list = []
        arguments = arg.split(" ")
        if arguments[0] == "":
            all_objects = storage.all()
            for obj_id in all_objects.keys():
                obj = all_objects[obj_id]
                objs_list.append(str(obj))
            print(objs_list)
        elif arguments[0] in HBNBCommand.class_list:
            class_string = arguments[0]
            if arguments[0] == class_string:
                all_objects = storage.all()
                for obj_id in all_objects.keys():
                    obj = all_objects[obj_id]
                    if obj.__class__.__name__ == class_string:
                        objs_list.append(str(obj))
                print(objs_list)
        else:
            print("** class doesn't exist **")

    def do_update(self, arg):
        'Updates an instance adding/updating attribute'
        arguments = arg.split(" ")
        if arguments[0] == "":
            print("** class name missing **")
        elif arguments[0] in HBNBCommand.class_list:
            class_string = arguments[0]
            if arguments[0] == class_string and len(arguments) == 1:
                print("** instance id missing **")
            elif len(arguments) == 2:
                all_objects = storage.all()
                switch = 0
                for obj_id in all_objects.keys():
                    obj = all_objects[obj_id]
                    if obj.id == arguments[1]:
                        print("** attribute name missing **")
                        switch = 1
                        break
                if switch == 0:
                    print("** no instance found **")
            elif len(arguments) == 3:
                print("** value missing **")
            else:
                if arguments[0] == class_string and len(arguments[1]) != 0:
                    all_objects = storage.all()
                    switch = 0
                    for obj_id in all_objects.keys():
                        obj = all_objects[obj_id]
                        if obj.id == arguments[1]:
                            string_cast = json.loads(arguments[3])
                            setattr(obj, arguments[2], string_cast)
                            storage.save()
                            switch = 1
                            break
                    if switch == 0:
                        print("** no instance found **")
        else:
            print("** class doesn't exist **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
