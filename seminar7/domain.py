import datetime
from abc import abstractmethod


class BaseEntity():
    def __init__(self, e_id):
        self.__id = e_id

    def get_id(self):
        return self.__id

    @classmethod
    def from_line(cls, line: str):
        raise NotImplementedError()

    @abstractmethod
    def to_line(self) -> str:
        pass


class Cat(BaseEntity):
    """
    Class for a cat
    """
    nr_instances = 0

    def __init__(self, c_id, name, race, weight):
        super().__init__(c_id)
        # print(f"Cat with name {name} was born")
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

    @classmethod
    def from_line(cls, line):
        fields = line.strip().split(',')
        c_id, name, race, weight = fields
        cat = Cat(c_id=int(c_id), name=name, race=race, weight=int(weight))
        return cat

    def to_line(self) -> str:
        return f"{self.get_id()},{self.get_name()},{self.get_race()},{self.get_weight()}\n"

    def __str__(self) -> str:
        return f"Cat(name={self.get_name()},race={self.__race},weight={self.__weight})"

    def __repr__(self) -> str:
        return str(self)

    def __lt__(self, other: Cat):
        return self.__weight < other.__weight

    def __eq__(self, value: object, /) -> bool:
        return self.get_id() == value.get_id()  # TODO fix this

    def __add__(self, other: Cat):
        first_half = self.__race[:len(self.__race) // 2]
        second_half = other.__race[len(other.__race) // 2:]
        return Cat(f"({self.get_name() + ' + ' + other.get_name()})", first_half + second_half,
                   100)  # for i in range(7)]


class Food(BaseEntity):
    def __init__(self, f_id, name: str, expiry: datetime.datetime, kcal: int):
        super().__init__(f_id)
        self.__name = name
        self.__expiry = expiry
        self.__kcal = kcal

    def get_name(self):
        return self.__name

    def get_expiry(self):
        return self.__expiry

    def get_kcal(self):
        return self.__kcal

    @classmethod
    def from_line(cls, line: str):
        fields = line.strip().split(',')
        f_id, name, expiry, kcal = fields
        expiry = list(map(int, expiry.split('/')))
        expiry = datetime.datetime(*expiry)  # destructuring
        food = Food(f_id=int(f_id), name=name, expiry=expiry, kcal=int(kcal))
        return food

    def to_line(self) -> str:
        expiry_str = self.get_expiry().strftime("%Y/%m/%d")
        food_line = f"{self.get_id()},{self.get_name()},{expiry_str},{self.get_kcal()}\n"
        return food_line

    def __str__(self) -> str:
        return f"Food(id={self.get_id()},name={self.get_name()},expiry={self.get_expiry()},kcal={self.get_kcal()})"


class Preference(BaseEntity):
    def __init__(self, pref_id, cat_id, food_id):
        super().__init__(pref_id)
        self.__cat_id = cat_id
        self.__food_id = food_id

    def get_cat_id(self):
        return self.__cat_id

    def get_food_id(self):
        return self.__food_id

    @classmethod
    def from_line(cls, line: str):
        fields = line.strip().split(',')
        pref_id, cat_id, food_id = fields
        preference = Preference(pref_id=int(pref_id), cat_id=int(cat_id), food_id=int(food_id))
        return preference

    def to_line(self) -> str:
        return f"{self.get_id()},{self.get_cat_id()},{self.get_food_id()}\n"

    def __str__(self) -> str:
        return f"Preference({self.get_id()},{self.get_cat_id()},{self.get_food_id()})"
