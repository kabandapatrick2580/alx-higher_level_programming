#!/usr/bin/python3
"""creation of a Base class"""
import json
import os


class Base:
    """representation of Base class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Base class initialization
        Args:
            id
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Method that returns json string representation
        Args:
            list_dictionaries(dict): list of dictionaries
        Return:
            JSON string
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        filename = cls.__name__ + ".json"
        with open(filename, 'w') as f:
            if list_objs == [] or None:
                json.dump(list_objs, filename)
            else:
                j_str = cls.to_json_string(
                    [obj.to_dictionary() for obj in list_objs]
                    )
                f.write(j_str)

    @staticmethod
    def from_json_string(json_string):
        """method that returns list of dictionaries
        Args:
            json_string (str): json string
        """
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Class method that returns an instance with attributes already set
        Args:
            **dictionary: representing the attributes
        Return:
            Instance with attributes already set
        """
        if cls.__name__ == "Rectangle":
            dummy_instance = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy_instance = cls(1)
        dummy_instance.update(**dictionary)
        return dummy_instance

    @classmethod
    def load_from_file(cls):
        """this is a Class method that returns a
        list of instances from a JSON file
        Return:
            List of instances
        """
        filename = cls.__name__ + ".json"
        instance_list = []

        if os.path.exists(filename):
            with open(filename, "r") as file:
                json_string = file.read()
                dict_list = json.loads(json_string)

            for dictionary in dict_list:
                instance = cls.create(**dictionary)
                instance_list.append(instance)

        return instance_list
