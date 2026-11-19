import datetime

from domain import Cat, Food, Preference
from seminar7.domain import Cat, Food


class RepositoryError(Exception):
    pass

class IDAlreadyExistsError(RepositoryError):
    pass

class EntityNotFoundError(RepositoryError):
    pass

class Repository:
    def __init__(self):
        self.__elements = {}

    # TODO as y'all can see, add, find_by_id and get_all are kinda repetitive
    #  We'll make sure next time to avoid that
    def add(self, elem):
        if elem.get_id() in self.__elements:
            raise IDAlreadyExistsError(f"ID {elem.get_id()} already exists")
        self.__elements[elem.get_id()]= elem

    def find_by_id(self, entity_id):
        for entity in self.get_all():
            if entity.get_id() == entity_id:
                return entity
        raise EntityNotFoundError(f"ID {entity_id} not found")


    def get_all(self):
        return list(self.__elements.values())

    def filter_by_weight(self, weight):
        return [cat for cat in self.get_all() if cat.get_weight() < weight]


class FileRepository(Repository):
    def __init__(self, file_name: str):
        super().__init__()
        self.__file_name = file_name
        self.__read_from_file()

    def __read_from_file(self):
        try:
            with open(self.__file_name,'r') as file:
                lines = file.readlines()
                for line in lines:
                    if not line.strip():
                        continue
                    fields = line.strip().split(',')
                    c_id, name, race, weight = fields
                    cat = Cat(c_id=int(c_id),name=name, race=race, weight=int(weight))
                    super().add(cat)
        except IOError as e:
            raise RepositoryError(e)

    def __write_to_file(self):
        with open(self.__file_name,'w') as file:
            for cat in self.get_all():
                cat_line = f"{cat.get_id()},{cat.get_name()},{cat.get_race()},{cat.get_weight()}\n"
                file.write(cat_line)


    def add(self, elem):
        super().add(elem)
        self.__write_to_file()

class FoodRepository:
    def __init__(self):
        self.__elements = {}

    def add(self, elem):
        if elem.get_id() in self.__elements:
            raise IDAlreadyExistsError(f"ID {elem.get_id()} already exists")
        self.__elements[elem.get_id()]= elem

    def find_by_id(self, entity_id):
        for entity in self.get_all():
            if entity.get_id() == entity_id:
                return entity
        raise EntityNotFoundError(f"ID {entity_id} not found")

    def get_all(self):
        return list(self.__elements.values())



class FoodFileRepository(FoodRepository):
    def __init__(self, file_name):
        super().__init__()
        self.__file_name = file_name
        self.__read_from_file()

    def __read_from_file(self):
        try:
            with open(self.__file_name,'r') as file:
                lines = file.readlines()
                for line in lines:
                    if not line.strip():
                        continue
                    fields = line.strip().split(',')
                    f_id, name, expiry, kcal = fields
                    expiry = list(map(int,expiry.split('/')))
                    expiry = datetime.datetime(*expiry) # destructuring
                    food = Food(f_id=int(f_id),name=name, expiry=expiry, kcal=int(kcal))
                    super().add(food)
        except IOError as e:
            raise RepositoryError(e)

    def __write_to_file(self):
        with open(self.__file_name,'w') as file:
            for food in self.get_all():
                expiry_str = food.get_expiry().strftime("%Y/%m/%d")
                food_line = f"{food.get_id()},{food.get_name()},{expiry_str},{food.get_kcal()}\n"
                file.write(food_line)

class PreferenceRepository:
    def __init__(self):
        self.__elements = {}

    def add(self, elem):
        if elem.get_id() in self.__elements:
            raise IDAlreadyExistsError(f"ID {elem.get_id()} already exists")
        self.__elements[elem.get_id()]= elem

    def find_by_id(self, entity_id):
        for entity in self.get_all():
            if entity.get_id() == entity_id:
                return entity
        raise EntityNotFoundError(f"ID {entity_id} not found")


    def get_all(self):
        return list(self.__elements.values())

class PreferenceFileRepository(PreferenceRepository):
    def __init__(self,file_name):
        super().__init__()
        self.__file_name = file_name
        self.__read_from_file()

    def __read_from_file(self):
        try:
            with open(self.__file_name,'r') as file:
                lines = file.readlines()
                for line in lines:
                    if not line.strip():
                        continue
                    fields = line.strip().split(',')
                    pref_id, cat_id, food_id = fields
                    preference = Preference(pref_id=int(pref_id), cat_id=int(cat_id), food_id=int(food_id))
                    super().add(preference)
        except IOError as e:
            raise RepositoryError(e)

    def __write_to_file(self):
        with open(self.__file_name,'w') as file:
            for pref in self.get_all():
                pref_line = f"{pref.get_id()},{pref.get_cat_id()},{pref.get_food_id()}\n"
                file.write(pref_line)


