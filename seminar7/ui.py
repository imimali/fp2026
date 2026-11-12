from seminar7.service import CatService


class UI:
    def __init__(self, service):
        self.__service = service

    @staticmethod
    def print_menu():
        print("1. Add cat")
        print("2. Filter by weight")
        print("0.exit")

    def read_valid_int(self, message: str = "Enter value: "):
        while True:
            try:
                return int(input(message))
            except ValueError:
                print("Invalid value, try again")

    def filter_by_weight_ui(self):
        weight = self.read_valid_int("Enter weight: ")
        thin_cats = self.__service.filter_by_weight(weight)
        for cat in thin_cats:
            print(cat)
        if not thin_cats:
            print("No such cats founds")

    def add_cat(self):
        name = input("Enter name: ")
        race = input("Enter race: ")
        weight = self.read_valid_int("Enter weight: ")
        self.__service.add(name, race, weight)
        print("Cat added successfully")

    def run(self):
        while True:
            self.print_menu()
            choice = input("Choose: ")
            match choice:
                case "1":
                    self.add_cat()
                case "2":
                    self.filter_by_weight_ui()
                case "0":
                    print("Bye")
                    break
