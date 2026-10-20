from domain import (create_cat)

from service import group_cats_by_race, get_cats_by_race, add_cat, update_cat, get_races


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
