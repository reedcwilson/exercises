
class Card(object):
    def __init__(self, pair):
        self.__numbers_map = {
            "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9,
            "10": 10, "J": 11, "Q": 12, "K": 13, "A": 14
        }
        self.__suit = pair[-1]
        self.__rank = int(self.__numbers_map[pair[0:-1]])

    @property
    def suit(self):
        return self.__suit

    @property
    def rank(self):
        return self.__rank


class Hand(object):
    def __init__(self, cards_str):
        self.__card_str = cards_str
        self.__cards = [Card(c) for c in cards_str.split()]
        self.__cards.sort(key=lambda c: c.rank)
        self.__rank = self._calculate_rank()

    def __str__(self):
        return self.__card_str

    def _is_four(self, counts):
        return counts == (4, 1)

    def _is_full_house(self, counts):
        return counts == (3, 2)

    def _is_flush(self):
        return len({c.suit for c in self.__cards}) == 1

    def _is_straight(self, counts, ranks):
        return (
            len(counts) == 5 and
            max(ranks) - min(ranks) == 4
        )

    def _is_three(self, counts):
        return counts == (3, 1, 1)

    def _is_two_pair(self, counts):
        return counts == (2, 2, 1)

    def _is_pair(self, counts):
        return counts == (2, 1, 1, 1)

    def _calculate_rank(self):
        ranks = [c.rank for c in self.__cards]
        counts, ranks = zip(*sorted(
            ((ranks.count(r), r) for r in set(ranks)),
            reverse=True
        ))
        # aces can start straight
        if ranks == (14, 5, 4, 3, 2):
            ranks = (5, 4, 3, 2, 1)
        if self._is_straight(counts, ranks) and self._is_flush():
            rank = 9
        elif self._is_four(counts):
            rank = 8
        elif self._is_full_house(counts):
            rank = 7
        elif self._is_flush():
            rank = 6
        elif self._is_straight(counts, ranks):
            rank = 5
        elif self._is_three(counts):
            rank = 4
        elif self._is_two_pair(counts):
            rank = 3
        elif self._is_pair(counts):
            rank = 2
        else:
            rank = 1
        # rank needs to be a sorted compound so we can resolve ties
        return (rank, ranks)

    @property
    def rank(self):
        return self.__rank


def best_hands(in_hands):
    hands = []
    for h in in_hands:
        hands.append(Hand(h))
    hands.sort(key=lambda h: h.rank, reverse=True)
    high = hands[0]
    return [str(h) for h in hands if h.rank == high.rank]
