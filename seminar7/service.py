from seminar7.domain import Cat, Food, Preference


class CatService:
    def __init__(self, repository):
        self.__repo = repository

    def add(self, c_id, name, race, weight):
        cat = Cat(c_id, name, race, weight)
        # todo validate
        self.__repo.add(cat)

    def filter_by_weight(self, weight):
        if weight < 0:
            raise ValueError("Invalid weight to filter by")
        return self.__repo.filter_by_weight(weight)

    def get_all(self):
        return self.__repo.get_all()


class FoodService:
    def __init__(self, repository):
        self.__repo = repository

    def add(self, f_id, name, expiry, kcal):
        food = Food(f_id, name, expiry, kcal)
        # todo validate
        self.__repo.add(food)

    def get_all(self):
        return self.__repo.get_all()


class PreferenceService:
    def __init__(self, repository, cat_repo, food_repo):
        self.__repo = repository
        self.__cat_repo = cat_repo
        self.__food_repo = food_repo

    def add(self, cat_id, food_id):
        preference = Preference(cat_id, food_id)
        self.__repo.add(preference)
        # todo validate

    def get_most_preferred_food(self):
        food_ids = [pref.get_food_id() for pref in self.__repo.get_all()]
        pref_stats = {}
        for food_id in food_ids:
            pref_stats[food_id] = 1 if food_id not in pref_stats else pref_stats[food_id] + 1
        if not pref_stats:
            raise ValueError("Cannot choose favorite food without any preferences")
        most_preferred = max(list(pref_stats.items()),
            key=lambda pair:pair[1])
        most_preferred_id = most_preferred[0]
        # todo define find by id
        return self.__food_repo.find_by_id(most_preferred_id)

    def get_all(self):
        return self.__repo.get_all()


