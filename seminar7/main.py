from seminar7.repository import CatFileRepository, FoodFileRepository, \
    PreferenceFileRepository
from seminar7.service import CatService, FoodService, PreferenceService
from seminar7.test import test_all
from seminar7.ui import UI

if __name__ == '__main__':
    test_all()

    cat_repo = CatFileRepository('cats.txt')
    food_repo = FoodFileRepository('foods.txt')
    preference_repo = PreferenceFileRepository('preferences.txt')
    cat_service = CatService(cat_repo)
    food_service = FoodService(food_repo)
    preference_service = PreferenceService(preference_repo, cat_repo, food_repo)
    ui = UI(cat_service, food_service, preference_service)
    ui.run()
