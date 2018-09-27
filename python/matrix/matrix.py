class Matrix(object):
    def __init__(self, string):
        self.matrix = [list(map(int, r.split())) for r in string.splitlines()]

    def row(self, index):
        return self.matrix[index]

    def column(self, index):
        return [r[index] for r in self.matrix]
