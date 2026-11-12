from seminar7.domain import Cat
from seminar7.repository import Repository
from seminar7.test import test_all
from seminar7.service import CatService
from seminar7.ui import UI
if __name__ == '__main__':
    test_all()

    repo = Repository()
    repo.add(Cat("aaa","black",1233))
    repo.add(Cat("aaa1","orange",455))
    repo.add(Cat("aaa2","black",111))
    repo.add(Cat("aaa3","tabbi",1233))
    repo.add(Cat("aaa4","british",678))
    repo.add(Cat("aaa5","black",567))
    service = CatService(repo)
    ui = UI(service)
    ui.run()
