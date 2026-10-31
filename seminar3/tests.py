from domain import (create_cat)
from copy import deepcopy
from service import (group_cats_by_race,
                     get_cats_by_race,
                     add_cat,
                     update_cat,
                     get_races,
                     save_state, average_weight, get_top_k_races, average_weight_for_top_k_races)


def test_get_cats_by_race():
    test_cats = []
    assert get_cats_by_race(test_cats, "orange") == []
    cat = create_cat("bober", "orange", 3500)
    add_cat(test_cats, cat)
    assert get_cats_by_race(test_cats, "orange") == [cat]
    assert get_cats_by_race(test_cats, "tabbi") == []
    tabbi = create_cat("bober2", "tabbi", 3500)
    add_cat(test_cats, tabbi)
    assert get_cats_by_race(test_cats, "orange") == [cat]
    assert get_cats_by_race(test_cats, "tabbi") == [tabbi]
    cat2 = create_cat("bober3", "orange", 3500)
    add_cat(test_cats, cat2)
    assert get_cats_by_race(test_cats, "orange") == [cat, cat2]
    assert get_cats_by_race(test_cats, "tabbi") == [tabbi]


def test_group_by_race():
    test_cats = []
    assert group_cats_by_race(test_cats) == {}
    cat = create_cat("bober", "orange", 3500)
    add_cat(test_cats, cat)
    assert group_cats_by_race(test_cats) == {"orange": ["bober"]}
    cat2 = create_cat("bober2", "orange", 3500)
    add_cat(test_cats, cat2)
    assert group_cats_by_race(test_cats) == {"orange": ["bober", "bober2"]}
    cat2 = create_cat("bober3", "tabbi", 3500)
    add_cat(test_cats, cat2)
    assert group_cats_by_race(test_cats) == {"orange": ["bober", "bober2"], "tabbi": ["bober3"]}


def test_get_races():
    test_cats = []
    assert get_races(test_cats) == set()
    cat = create_cat("bober", "orange", 3500)
    add_cat(test_cats, cat)
    assert get_races(test_cats) == {"orange"}
    add_cat(test_cats, create_cat("bober2", "tabbi", 3500))
    assert get_races(test_cats) == {"orange", "tabbi"}
    add_cat(test_cats, create_cat("bober3", "orange", 3500))
    assert get_races(test_cats) == {"orange", "tabbi"}


def test_add_cat():
    test_cats = []
    cat = create_cat("bober", "orange", 3500)
    add_cat(test_cats, cat)
    assert len(test_cats) == 1
    assert test_cats[0] == cat


def test_update_cat():
    test_cats = []
    cat = create_cat("bober", "orange", 3500)
    add_cat(test_cats, cat)
    try:
        update_cat(test_cats, create_cat("noname", "", 0))
        assert False
    except ValueError:
        assert True

    cat2 = create_cat("bober", "gray", 5000)
    update_cat(test_cats, cat2)
    assert test_cats[0] == cat2


def test_save_state():
    test_cats = []
    test_undo_stack = []
    save_state(test_undo_stack, test_cats)
    assert test_undo_stack == [[]]
    prev_undo_stack = deepcopy(test_undo_stack)

    cat = create_cat("bober", "orange", 3500)
    add_cat(test_cats, cat)
    save_state(test_undo_stack, test_cats)
    # assert test_undo_stack == [[],[cat]]
    expected = deepcopy(prev_undo_stack)
    expected.append(deepcopy(test_cats))
    assert test_undo_stack == expected
    prev_undo_stack = deepcopy(test_undo_stack)

    cat2 = create_cat("bober", "orange2", 3700)
    update_cat(test_cats, cat2)
    save_state(test_undo_stack, test_cats)
    expected = deepcopy(prev_undo_stack)
    expected.append(deepcopy(test_cats))
    assert test_undo_stack == expected


def test_average_weight():
    cats = []
    assert average_weight(cats) == .0
    cats = [create_cat("bober", "orange", 3500)]
    assert average_weight(cats) == 3500
    cats.append(create_cat("bober", "orange", 3500))
    assert average_weight(cats) == 3500
    cats.append(create_cat("bober", "orange", 2000))
    assert average_weight(cats) == 3000


def test_top_k_races():
    cats = []
    assert get_top_k_races(cats) == []
    cats = [create_cat("bober", "orange", 3500)]
    assert get_top_k_races(cats) == ["orange"]

    cats = [
        create_cat("bober", "orange", 3500),
        create_cat("bober", "red", 3500),
        create_cat("bober", "white", 3500),
    ]

    assert get_top_k_races(cats) == ["white", "red", "orange"]

    cats = [
        create_cat("bober", "orange", 3500),
        create_cat("bober", "orange", 3500),
        create_cat("bober", "red", 3500),
        create_cat("bober", "white", 3500),
    ]

    assert get_top_k_races(cats) == ["orange", "white", "red", ]


def test_average_weight_of_top_k_races():
    cats = []
    assert average_weight_for_top_k_races(cats) == {}
    cats = [create_cat("bober", "orange", 3500)]
    assert average_weight_for_top_k_races(cats) == {"orange": 3500}
    #
    cats = [
        create_cat("bober", "orange", 3500),
        create_cat("bober", "red", 3500),
        create_cat("bober", "white", 3500),
    ]
    assert average_weight_for_top_k_races(cats) == {"orange": 3500, "red": 3500, "white": 3500}
    #
    cats = [
        create_cat("bober", "orange", 3500),
        create_cat("bober", "orange", 4500),
        create_cat("bober", "red", 3500),
        create_cat("bober", "white", 3500),
    ]
    #
    assert average_weight_for_top_k_races(cats) == {"orange":4000,"white":3500, "red":3500}
