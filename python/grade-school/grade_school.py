class School(object):
    def __init__(self, name):
        self.__grades = {}

    def add(self, name, num):
        self.__grades.setdefault(num, set()).add(name)

    def grade(self, grade_num):
        return set(self.__grades.get(grade_num, set()))

    def sort(self):
        return [(i, tuple(sorted(g))) for i, g in self.__grades.items()]
