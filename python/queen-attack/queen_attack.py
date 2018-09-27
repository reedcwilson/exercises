class Queen(object):
    def __init__(self, row, column):
        if row < 0 or column < 0 or row > 7 or column > 7:
            raise ValueError('invalid position')
        self.coord = (row, column)

    def can_attack(self, piece):
        if self.coord == piece.coord:
            raise ValueError('pieces\' positions match')
        return (
            self.coord[0] == piece.coord[0]
            or self.coord[1] == piece.coord[1]
            or len({abs(a - b) for a, b in zip(self.coord, piece.coord)}) == 1
        )
