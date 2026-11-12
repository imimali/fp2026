class Repository:
    def __init__(self):
        self.__elements = []

    def add(self, elem):
        # todo verify ID uniqueness if entered by hand
        self.__elements.append(elem)

    def get_all(self):
        return self.__elements

    def filter_by_weight(self, weight):
        return [cat for cat in self.__elements if cat.get_weight()< weight]
