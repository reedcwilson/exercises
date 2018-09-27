class Phone(object):
    def __init__(self, number):
        self.__ac, self.__ex, self.__sub = self._get_parts(number)
        self._valid(self.area_code)
        self._valid(self.exchange)

    def _valid(self, part):
        if part[0] == '0' or part[0] == '1':
            raise ValueError('area codes & exchanges cannot start with 0 or 1')

    def _get_parts(self, number):
        numbers = ''.join([c for c in number if c.isdigit()])
        numbers_count = len(numbers)
        if not 9 < numbers_count < 12:
            raise ValueError('phone number is the wrong length')
        if numbers_count == 11:
            if numbers[0] != '1':
                raise ValueError('invalid country code: {}'.format(numbers[0]))
            numbers = numbers[1:]
        return numbers[0:3], numbers[3:6], numbers[6:]

    @property
    def area_code(self):
        return self.__ac

    @property
    def exchange(self):
        return self.__ex

    @property
    def subscriber(self):
        return self.__sub

    @property
    def number(self):
        return ''.join([
            self.area_code,
            self.exchange,
            self.subscriber
        ])

    def pretty(self):
        return '({}) {}-{}'.format(
            self.area_code,
            self.exchange,
            self.subscriber
        )
