from seminar7.domain import Cat
class CatService:
    def __init__(self, repository):
        self.__repo = repository

    def add(self, name, race, weight):
        cat = Cat(name, race, weight)
        # todo validate
        self.__repo.add(cat)

    def filter_by_weight(self, weight):
        if weight < 0:
            raise ValueError("Invalid weight to filter by")
        return self.__repo.filter_by_weight(weight)
