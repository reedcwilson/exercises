

allergies = [
    'eggs',
    'peanuts',
    'shellfish',
    'strawberries',
    'tomatoes',
    'chocolate',
    'pollen',
    'cats',
]


class Allergies(object):

    def __init__(self, score):
        self.score = score

    def is_allergic_to(self, item):
        return self.score & (1 << allergies.index(item)) > 0

    @property
    def lst(self):
        return [a for a in allergies if self.is_allergic_to(a)]
