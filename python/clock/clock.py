class Clock(object):
    def __init__(self, hour, minute):
        self.hour, self.minute = divmod((hour * 60 + minute) % (24 * 60), 60)

    def __repr__(self):
        return f'{self.hour:02d}:{self.minute:02d}'

    def __eq__(self, other):
        return self.hour == other.hour and self.minute == other.minute

    def __add__(self, minutes):
        return Clock(self.hour, self.minute + minutes)

    def __sub__(self, minutes):
        return Clock(self.hour, self.minute - minutes)
