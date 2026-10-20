from domain import (get_race,
                    get_name,
                    get_weight,
                    set_weight,
                    set_race)

def add_cat(cats: list, cat):
    cats.append(cat)


def update_cat(cats, new_cat):
    """
    Finds cat by name and changes the rest of the fields
    :param cats:
    :param new_cat:
    :return:
    """
    found_cat = None
    for cat in cats:
        if get_name(cat) == get_name(new_cat):
            found_cat = cat
    if found_cat is None:
        raise ValueError(f"Cat named {get_name(new_cat)} not found")

    # found_cat["race"] = new_cat["race"]
    set_race(found_cat, get_race(new_cat))
    set_weight(found_cat, get_weight(new_cat))


def get_races(cats):
    # return set(map(get_race,cats))
    all_races = []
    for cat in cats:
        all_races.append(get_race(cat))
    return set(all_races)


def get_cats_by_race(cats, race):
    # return list(filter,lambda cat:get_race(cat)==race,cats)
    # return [cat for cat in cats if get_race(cat)==race]
    filtered = []
    for cat in cats:
        if get_race(cat) == race:
            filtered.append(cat)
    return filtered


def group_cats_by_race(cats):
    """
    returns a dictionary of the form: {race: [name1, name2], ...}
    :param cats:
    :return:
    """
    # res = {}
    # for cat in cats:
    #     if get_race(cat) not in res:
    #         res[get_race(cat)] = []
    #     res[get_race(cat)].append(get_name(cat))
    races = get_races(cats)
    result = dict()
    for race in races:
        cats_of_race = get_cats_by_race(cats, race)
        cat_names = [get_name(cat) for cat in cats_of_race]
        result[race] = cat_names
    return result
