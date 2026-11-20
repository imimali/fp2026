import datetime

from domain import Cat, Food, Preference
from seminar7.domain import Cat, Food, BaseEntity


class RepositoryError(Exception):
    pass


class IDAlreadyExistsError(RepositoryError):
    pass


class EntityNotFoundError(RepositoryError):
    pass


class BaseRepository:
    def __init__(self):
        self.__elements = {}

    def add(self, elem: BaseEntity):
        if elem.get_id() in self.__elements:
            raise IDAlreadyExistsError(f"ID {elem.get_id()} already exists")
        self.__elements[elem.get_id()] = elem

    def find_by_id(self, entity_id):
        for entity in self.get_all():
            if entity.get_id() == entity_id:
                return entity
        raise EntityNotFoundError(f"ID {entity_id} not found")

    def get_all(self):
        return list(self.__elements.values())

    def filter_by_weight(self, weight):
        return [cat for cat in self.get_all() if cat.get_weight() < weight]


class BaseFileRepository(BaseRepository):
    def __init__(self, file_name: str, clazz: type[BaseEntity]):
        super().__init__()
        self.__file_name = file_name
        self.__class = clazz
        self.__read_from_file()

    def __read_from_file(self):
        try:
            with open(self.__file_name, 'r') as file:
                lines = file.readlines()
                for line in lines:
                    if not line.strip():
                        continue
                    entity = self.__class.from_line(line)
                    super().add(entity)
        except IOError as e:
            raise RepositoryError(e)

    def __write_to_file(self):
        with open(self.__file_name, 'w') as file:
            for entity in self.get_all():
                entity_line = entity.to_line()
                file.write(entity_line)

    def add(self, elem):
        super().add(elem)
        self.__write_to_file()



class CatFileRepository(BaseFileRepository):
    def __init__(self, file_name: str):
        super().__init__(file_name, Cat)


class FoodFileRepository(BaseFileRepository):
    def __init__(self, file_name):
        super().__init__(file_name, Food)


class PreferenceFileRepository(BaseFileRepository):
    def __init__(self, file_name):
        super().__init__(file_name, Preference)
