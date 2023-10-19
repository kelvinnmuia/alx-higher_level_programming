#!/usr/bin/python3
"""defines the Base class"""
import csv


class Base():
    """manages the id attribute in future classes"""
    __nb_objects = 0

    def __init__(self, id=None):
        """initializes class nb_objects"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns JSON string representation
        of the list of dictionaries"""
        import json
        if list_dictionaries is None:
            return "[]"
        if len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list
        of instances who inherists from Base to a file"""
        if list_objs is None:
            list_objs = []
        filename = cls.__name__ + ".json"
        list_dictionaries = []
        for instance in list_objs:
            list_dictionaries.append(instance.to_dictionary())
        with open(filename, 'w') as f:
            f.write(cls.to_json_string(list_dictionaries))

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string
        representation for list of dictionaries"""
        import json
        if json_string is None:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes
        already set using update method"""
        if cls.__name__ == "Rectangle":
            instance = cls(1, 1, 0, 0)
        if cls.__name__ == "Square":
            instance = cls(1, 0, 0)
        instance.update(**dictionary)
        return instance

    @classmethod
    def load_from_file(cls):
        """return list of instances from file
        containing saved JSON string"""
        filename = cls.__name__ + ".json"
        results = []
        try:
            with open(filename, 'r') as f:
                for instance in cls.from_json(f.read()):
                    results.append(cls.create(**instance))
        except Exception as err:
            pass
        return (results)

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serialize and save objects to a CSV file."""
        file_name = cls.__name__ + '.csv'
        with open(file_name, 'w', newline='') as csvfile:
            if list_objs:
                fieldnames = list_objs[0].to_dict().keys()
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                for obj in list_objs:
                    writer.writerow(obj.to_dict())

    @classmethod
    def load_from_file_csv(cls):
        """Deserialize and load objects from a CSV file."""
        file_name = cls.__name__ + '.csv'
        obj_list = []
        try:
            with open(file_name, 'r') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    obj_dict = {k: int(v) for k, v in row.items()}
                    obj_list.append(cls.create(**obj_dict))
            return obj_list
        except FileNotFoundError:
            return []

    def to_dict(self):
        """Convert object attributes to a dictionary."""
        return {attr: getattr(self, attr) for attr in
                self.__dict__ if not callable(getattr(self, attr))}
