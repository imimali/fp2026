from domain import (get_race,
                    get_name,
                    get_weight,
                    set_weight,
                    set_race)

def add_cat(cats: list, cat):
    # TODO verify uniqueness of name or introduce ids
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


def get_cats_by_race(cats, race) -> list:
    # return list(filter,lambda cat:get_race(cat)==race,cats)
    # return [cat for cat in cats if get_race(cat)==race]
    filtered = []
    for cat in cats:
        if get_race(cat) == race:
            filtered.append(cat)
    return filtered

def average_weight(cats):
    if not cats:
        return 0.0
    weights = []
    for cat in cats:
        weights.append(get_weight(cat))
    return sum(weights)/len(weights)

def get_top_k_races(cats,k=3):
    races = get_races(cats)
    nr_cats_by_race = {}
    for race in races:
        nr_cats = len(get_cats_by_race(cats, race))
        nr_cats_by_race[race] = nr_cats

    # def get_nr(race):
    #     return nr_cats_by_race[race]
    # sorted_races = sorted(nr_cats_by_race.keys(), key=get_race,reverse=True)
    sorted_races = sorted(nr_cats_by_race.keys(),
                          key=lambda r:[nr_cats_by_race[r],r],
                          reverse=True)
    return sorted_races[:k]


def average_weight_for_top_k_races(cats, k=3):
    top_k_races = get_top_k_races(cats,k)
    result = {}
    for race in top_k_races:
        cats_of_race = get_cats_by_race(cats,race)
        result[race]= average_weight(cats_of_race)
    return result





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


def save_state(undo_stack:list, cats:list):
    copied_cats = []
    for cat in cats:
        copied_cats.append(cat.copy())
    undo_stack.append(copied_cats)

def perform_undo(undo_stack:list, cats:list):
    if not undo_stack:
        raise ValueError("Nothing to undo!")
    last_state = undo_stack.pop()
    cats[:] = last_state




