class Unique(object):
    __ignore_case = False
    __items = []
    __iter = iter(__items)

    def __init__(self, items, **kwargs):
        self.__ignore_case = False
        self.__items = []
        self.__iter = iter(self.__items)

        if 'ignore_case' in kwargs:
            self.__ignore_case = bool(kwargs['ignore_case'])

        for item in items:
            if type(item) == type('') and self.__ignore_case:
                if not any(str(x).lower() == item.lower() for x in self.__items):
                    self.__items.append(item)
            else:
                if not item in self.__items:
                    self.__items.append(item)

    def __next__(self):
        return next(self.__iter)

    def __iter__(self):
        return self.__iter

    def ignore_case(self):
        return self.__ignore_case