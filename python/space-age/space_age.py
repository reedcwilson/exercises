class SpaceAge(object):
    def __init__(self, seconds):
        self.__seconds = seconds
        periods = zip(
            ['earth', 'mercury', 'venus', 'mars', 'jupiter', 'saturn', 'uranus', 'neptune'],
            [1, 0.2408467, 0.61519726, 1.8808158, 11.862615, 29.447498, 84.016846, 164.79132]
        )
        earth_period = seconds / 31557600
        func_str = 'self.on_{} = lambda: round({}/{}, 2)'
        for planet, period in periods:
            exec(func_str.format(planet, earth_period, period))

    @property
    def seconds(self):
        return round(self.__seconds, 2)
