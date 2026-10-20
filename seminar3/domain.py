def get_weight(cat: dict):
    return cat["weight"]


def get_name(cat: dict):
    return cat["name"]


def get_race(cat: dict):
    return cat["race"]


def create_cat(name, race, weight):
    return dict(name=name, race=race, weight=weight)


def set_name(cat, name):
    cat['name'] = name


def set_race(cat, race):
    cat['race'] = race


def set_weight(cat, weight):
    cat['weight'] = weight
