
default_students = [
    "Alice", "Bob", "Charlie", "David", "Eve", "Fred", "Ginny", "Harriet",
    "Ileana", "Joseph", "Kincaid", "Larry",
]

plants = {"G": "Grass", "C": "Clover", "R": "Radishes", "V": "Violets"}


class Garden(object):
    def __init__(self, diagram, students=default_students):
        self.rows = diagram.split('\n')
        self.students = sorted(students)

    def plants(self, student):
        i = self.students.index(student) * 2
        return [e for r in self.rows for e in [plants[r[i]], plants[r[i+1]]]]
