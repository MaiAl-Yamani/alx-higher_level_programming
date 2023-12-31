#!/usr/bin/python3
"""This is base.py module."""
import json
import os.path
import csv


class Base:
    """This is Base class."""
    __nb_objects = 0

    def __init__(self, id=None):
        """Instantiation method."""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries."""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Rrites the JSON string representation of list_objs to a file."""
        filename = str(cls.__name__) + ".json"
        with open(filename, mode="w", encoding="utf-8") as f:
            my_list = []
            if list_objs is None:
                f.write(cls.to_json_string(my_list))
            else:
                for i in range(len(list_objs)):
                    my_list.append(list_objs[i].to_dictionary())
                f.write(cls.to_json_string(my_list))

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation json_string."""
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set."""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        if cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances."""
        if not os.path.exists(cls.__name__ + ".json"):
            return []
        filename = str(cls.__name__) + ".json"
        with open(filename, encoding="utf-8") as f:
            my_dicts_list = cls.from_json_string(f.read())
            instances = [cls.create(**my_dict) for my_dict in my_dicts_list]
        return instances

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """save to csv file."""
        filename = cls.__name__ + ".csv"
        if cls.__name__ == "Rectangle":
            csv_format = ["id", "width", "height", "x", "y"]
        if cls.__name__ == "Square":
            csv_format = ["id", "size", "x", "y"]

        with open(filename, mode="w") as data_file:
            writer = csv.DictWriter(data_file, fieldnames=csv_format)
            [writer.writerow(item.to_dictionary()) for item in list_objs]

    @classmethod
    def load_from_file_csv(cls):
        """load from csv file."""
        filename = cls.__name__ + ".csv"
        if not os.path.exists(filename):
            return []
        ret_list = []
        my_dict_csv = {}
        if cls.__name__ == "Rectangle":
            csv_format = ['id', 'width', 'height', 'x', 'y']
        else:
            csv_format = ['id', 'size', 'x', 'y']

        with open(filename, mode="r") as fd:
            reader = csv.DictReader(fd, fieldnames=csv_format)
            for item in reader:
                for key in item:
                    my_dict_csv[key] = int(item[key])
                ret_list.append(cls.create(**my_dict_csv))
        return ret_list
