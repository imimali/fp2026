"""
{"name":"","race":"","weight":...}
[name, race,weight]
1. add
2. update
3. group by race  orange: bubu, bober
                  black: ..., ...


- list of lists (list of states)
cats = [], undo_stack = []
...adaug o pisică
cats = [cat], undo_stack = [[]]
... modific pisica
cats = [cat'], undo_stack = [[],[cat]]
... undo
cat = [cat], undo_stack = [[]]

Get the average weight for each of the top
3 most popular (with the most individuals) races
"""
from domain import (create_cat)
from seminar3.service import perform_undo
from seminar3.tests import test_add_cat, test_update_cat, test_get_races, test_get_cats_by_race, test_group_by_race, \
    test_save_state, test_average_weight, test_top_k_races, test_average_weight_of_top_k_races
from seminar3.validation import validate_string

from service import group_cats_by_race, add_cat, update_cat, save_state

def read_valid_int(message):
    while True:
        try:
            return int(input(message))
        except ValueError:
            print("Invalid value! Try again")

def read_valid_string(message):
    while True:
        try:
            value= input(message)
            validate_string(value)
            return value
        except Exception:
            print("Invalid value! Try again")

def read_cat():
    name = read_valid_string("Enter name: ")
    race = read_valid_string("Enter race: ")
    weight = read_valid_int("Enter weight: ")
    return create_cat(name, race, weight)


def run():
    print("1. Add cat")
    print("2. Update cat")
    print("3. Group by race")
    print("4. Undo")
    print("0. Exit")
    cats = []
    undo_stack = []
    # for cat_index in range(10_000_000):
    #     add_cat(cats, create_cat(
    #         f"cat{cat_index}",f"race{cat_index}",cat_index*10))
    # print("All cats added")

    add_cat(cats, create_cat("bober", "orange", 3500))
    add_cat(cats, create_cat("bober1", "tabbi", 3500))
    add_cat(cats, create_cat("bober2", "orange2", 3500))
    add_cat(cats, create_cat("bober3", "tabbi", 3500))
    while True:
        try:
            option = input("Choose: ")
            match option:
                case "1":
                    save_state(undo_stack, cats)
                    cat = read_cat()
                    add_cat(cats, cat)
                    print("Cat added successfully")
                case "2":
                    save_state(undo_stack, cats)
                    new_cat = read_cat()
                    update_cat(cats, new_cat)
                    print("Cat updated successfully")

                case "3":
                    result = group_cats_by_race(cats)
                    for race in result:
                        print(race, end=": ")
                        for name in result[race]:
                            print(name, end=", ")
                        print()
                case "4":
                    perform_undo(undo_stack,cats)

                case "0":
                    exit(0)
                case _:
                    print("Invalid option")
        except Exception as e:
            print(f"Error occurred: {e}")


if __name__ == '__main__':
    test_add_cat()
    test_update_cat()
    test_get_races()
    test_get_cats_by_race()
    test_group_by_race()
    test_save_state()

    test_average_weight()
    test_top_k_races()
    test_average_weight_of_top_k_races()
    run()
