import random
import time
import datetime


class Cat:
    """
    Class for a cat
    """
    nr_instances = 0

    def __init__(self, c_id, name, race, weight):
        self.__id = c_id
        # print(f"Cat with name {name} was born")
        self.__name = name
        self.__race = race
        self.__weight = weight
        Cat.nr_instances += 1

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_race(self):
        return self.__race

    def get_weight(self):
        return self.__weight

    def set_name(self, name):
        self.__name = name

    def __str__(self) -> str:
        return f"Cat(name={self.get_name()},race={self.__race},weight={self.__weight})"

    def __repr__(self) -> str:
        return str(self)

    def __lt__(self, other: Cat):
        return self.__weight < other.__weight

    def __eq__(self, value: object, /) -> bool:
        return self.__id == value.__id  # TODO fix this

    def __add__(self, other: Cat):
        first_half = self.__race[:len(self.__race) // 2]
        second_half = other.__race[len(other.__race) // 2:]
        return Cat(f"({self.get_name() + ' + ' + other.get_name()})", first_half + second_half,
                   100)  # for i in range(7)]


class Food():
    def __init__(self, f_id, name: str, expiry: datetime.datetime, kcal: int):
        self.__id = f_id
        self.__name = name
        self.__expiry = expiry
        self.__kcal = kcal

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_expiry(self):
        return self.__expiry

    def get_kcal(self):
        return self.__kcal

    def __str__(self) -> str:
        return f"Food(id={self.get_id()},name={self.get_name()},expiry={self.get_expiry()},kcal={self.get_kcal()})"



class Preference:
    def __init__(self,pref_id, cat_id, food_id):
        self.__pref_id = pref_id
        self.__cat_id = cat_id
        self.__food_id = food_id

    def get_id(self):
        return self.__pref_id

    def get_cat_id(self):
        return self.__cat_id

    def get_food_id(self):
        return self.__food_id

    def __str__(self) -> str:
        return f"Preference({self.get_id()},{self.get_cat_id()},{self.get_food_id()})"
