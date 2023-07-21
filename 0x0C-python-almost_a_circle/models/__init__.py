#!/usr/bin/python3

import json
import csv
from dataclasses import dataclass


@dataclass
class Base:
    id: int

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        filename = cls.__name__ + ".json"
        list_dicts = [obj.__dict__ for obj in list_objs] if list_objs else []
        with open(filename, "w") as jsonfile:
            jsonfile.write(cls.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        if not json_string or json_string == "[]":
            return []
    return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        new = cls(1)
        new.__dict__.update(dictionary)
        return new

    @classmethod
    def load_from_file(cls):
        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r") as jsonfile:
                list_dicts = cls.from_json_string(jsonfile.read())
                return [cls.create(**d) for d in list_dicts]
        except IOError
        return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        filename = cls.__name__ + ".csv"
        fieldnames = list_objs[0].__dict__.keys() if list_objs else []
        with open(filename, "w", newline="") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for obj in list_objs:
                writer.writerow(obj.__dict__)

    @classmethod
    def load_from_file_csv(cls):
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline="") as csvfile:
                reader = csv.DictReader(csvfile)
                return [cls.create(**row) for row in reader]
        except IOError:
            return []


class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def to_dictionary(self):
        return self.__dict__


class Square(Base):
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(id)
        self.size = size
        self.x = x
        self.y = y

    def to_dictionary(self):
        return self.__dict__

    if __name__ == "__main__":
        rectangles = [Rectangle(10, 5, 1, 2), Rectangle(7, 3, 4, 8)]
        squares = [Square(5, 3, 3), Square(2, 1, 1)]

        Base.save_to_file(rectangles)
        Base.save_to_file_csv(squares)

        loaded_rectangles = Rectangle.load_from_file()
        loaded_squares = Square.load_from_file_csv()

    print("Loaded rectangles:")
    for rectangle in loaded_rectangles:
        print(rectangle.__dict__)

    print("\nLoaded squares:")
    for square in loaded_squares:
        print(square.__dict__)
