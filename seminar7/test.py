from domain import Cat
from repository import Repository
from seminar7.validator import CatValidator, ValidationError
from service import CatService
def test_repo_add():
    repo = Repository()
    cat = Cat("aa","black",1233)
    repo.add(cat)
    assert repo.get_all() == [cat]

def test_service_add():
    repo = Repository()
    service = CatService(repo)
    service.add("aa","black",1233)
    assert repo.get_all()[0].get_name() == "aa"
    ...

def test_cat_validator():
    cat = Cat("aaa","orange",1234)
    CatValidator.validate(cat)
    try:
        CatValidator.validate(Cat("","black",1255))
        assert False, "Exception should have been thrown"
    except ValidationError as e:
        assert str(e)== "Name cannot be void"
    # todo test other cases

def test_repo_filter_by_weight():
    repo = Repository()

    assert repo.filter_by_weight(100012313) == []

    cat = Cat("aa", "black", 500)
    cat1 = Cat("aa1", "orange", 233)
    cat2 = Cat("aa2", "tabbi", 1000)
    cat3 = Cat("aa3", "british", 100_000)
    for c in [cat,cat1,cat2, cat3]:
        repo.add(c)
    assert repo.filter_by_weight(501) == [cat, cat1]
    assert repo.filter_by_weight(500) == [cat1]
    assert repo.filter_by_weight(200_000) == [cat,cat1,cat2, cat3]

def test_service_filter_by_weight():
    repo = Repository()
    service = CatService(repo)
    assert service.filter_by_weight(100012313) == []

    cat = Cat("aa", "black", 500)
    cat1 = Cat("aa1", "orange", 233)
    cat2 = Cat("aa2", "tabbi", 1000)
    cat3 = Cat("aa3", "british", 100_000)
    for c in [cat,cat1,cat2, cat3]:
        repo.add(c)
    assert service.filter_by_weight(501) == [cat, cat1]
    assert service.filter_by_weight(500) == [cat1]
    assert service.filter_by_weight(200_000) == [cat,cat1,cat2, cat3]

def test_all():
    test_repo_add()
    test_service_add()
    test_cat_validator()
    test_repo_filter_by_weight()
    test_service_filter_by_weight()

