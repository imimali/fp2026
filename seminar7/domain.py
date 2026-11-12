import random
import time


class Cat:
    """
    Class for a cat
    """
    nr_instances = 0

    def __init__(self, name, race, weight):
        self.__id = Cat.nr_instances
        #print(f"Cat with name {name} was born")
        self.__name = name
        self.__race = race
        self.__weight = weight
        Cat.nr_instances += 1

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

    def __lt__(self, other:Cat):
        return self.__weight < other.__weight

    def __eq__(self, value: object, /) -> bool:
        return self.__id == value.__id # TODO fix this

    def __add__(self, other: Cat):
        first_half = self.__race[:len(self.__race)//2]
        second_half = other.__race[len(other.__race)//2:]
        return Cat(f"({self.get_name()+' + '+other.get_name()})",first_half+second_half,100)# for i in range(7)]
