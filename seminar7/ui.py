from seminar7.service import CatService


class UI:
    def __init__(self, cat_service, food_service, preference_service):
        self.__cat_service = cat_service
        self.__food_service = food_service
        self.__preference_service = preference_service

    @staticmethod
    def print_menu():
        print("1.c - Add cat")
        print("1.f - Add food")
        print("2 - Filter cats by weight")
        print("3 - Most preferred food")
        print("3.c - See all cats")
        print("3.f - See all foods")
        print("3.p - See all preferences")
        print("0 - exit")

    def read_valid_int(self, message: str = "Enter value: "):
        while True:
            try:
                return int(input(message))
            except ValueError:
                print("Invalid value, try again")

    def filter_by_weight_ui(self):
        weight = self.read_valid_int("Enter weight: ")
        thin_cats = self.__cat_service.filter_by_weight(weight)
        for cat in thin_cats:
            print(cat)
        if not thin_cats:
            print("No such cats founds")

    def add_cat(self):
        c_id = self.read_valid_int("Enter id: ")
        name = input("Enter name: ")
        race = input("Enter race: ")
        weight = self.read_valid_int("Enter weight: ")
        self.__cat_service.add(c_id, name, race, weight)
        print("Cat added successfully")

    def add_food(self):
        f_id = self.read_valid_int("Enter id: ")
        name = input("Enter name: ")
        expiry = input("Enter expiry: ")
        kcal = self.read_valid_int("Enter kcal: ")
        self.__food_service.add(f_id, name, expiry, kcal)
        print("Food added successfully")

    def most_preferred_food(self):
        most_preferred = self.__preference_service.get_most_preferred_food()
        print("Most preferred food is", most_preferred)

    def run(self):
        while True:
            self.print_menu()
            choice = input("Choose: ")
            match choice:
                case "1.c":
                    self.add_cat()
                case "1.f":
                    self.add_food()
                case "2":
                    self.filter_by_weight_ui()

                case "3":
                    self.most_preferred_food()

                case "3.c":
                    for cat in self.__cat_service.get_all():
                        print(cat)

                case "3.f":
                    for food in self.__food_service.get_all():
                        print(food)
                case "3.p":
                    for preference in self.__preference_service.get_all():
                        print(preference)
                case "0":
                    print("Bye")
                    break
