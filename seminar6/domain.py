import random
import time


class Cat:
    """
    Class for a cat
    """
    nr_instances = 0

    def __init__(self, name, race, weight):
        self.__id = Cat.nr_instances
        print(f"Cat with name {name} was born")
        self.__name = name
        self.__race = race
        self.__weight = weight
        self.__health = 100
        Cat.nr_instances += 1

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_health(self):
        return self.__health

    def take_damage(self, damage):
        self.__health -= damage

    def attack(self, other: Cat):
        damage = random.randint(1, 20)
        other.take_damage(damage)
        print(f"{self.get_name()} attacked {other.get_name()} and is down to {other.get_health()}")
        time.sleep(1)

    def __str__(self) -> str:
        return f"Cat(name={self.get_name()},race={self.__race},weight={self.__weight},health={self.get_health()})"

    def __repr__(self) -> str:
        return str(self)

    def __lt__(self, other:Cat):
        return self.__weight < other.__weight

    def __eq__(self, value: object, /) -> bool:
        return self.__id == value.__id # TODO fix this

    def __add__(self, other:Cat):
        first_half = self.__race[:len(self.__race)//2]
        second_half = other.__race[len(other.__race)//2:]
        return Cat(f"({self.get_name()+' + '+other.get_name()})",first_half+second_half,100)# for i in range(7)]

if __name__ == '__main__':
    cat = Cat("Dark", "black", 5000)
    cat4 = Cat("Dark", "black", 5000)
    cat2 = Cat("Gandalf", "white", 4000)
    cat3 = Cat("Gandalfer", "whhhhh", 5000)
    print(f"{cat.get_name()} vs {cat2.get_name()} started")
    print(cat>cat2)
    print(cat+cat2+cat3)
    print(cat==cat4)
    # cat, cat2 = (cat, cat2) if random.random() >= 0.5 else (cat2, cat)
    # while cat.get_health() >= 30 and cat2.get_health() >= 30:
    #     cat.attack(cat2)
    #     cat2.attack(cat)
    # winner = cat if cat.get_health() > cat2.get_health() else cat2
    # print(winner)
