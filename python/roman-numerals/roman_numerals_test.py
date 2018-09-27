import unittest

import roman_numerals


# Tests adapted from `problem-specifications//canonical-data.json` @ v1.0.0

class RomanTest(unittest.TestCase):

    numerals = {
        1: 'I',
        2: 'II',
        3: 'III',
        4: 'IV',
        5: 'V',
        6: 'VI',
        9: 'IX',
        27: 'XXVII',
        48: 'XLVIII',
        59: 'LIX',
        93: 'XCIII',
        141: 'CXLI',
        163: 'CLXIII',
        402: 'CDII',
        575: 'DLXXV',
        911: 'CMXI',
        1024: 'MXXIV',
        3000: 'MMM',
    }

    # def test_numerals(self):
    #     for arabic, numeral in self.numerals.items():
    #         self.assertEqual(roman_numerals.numeral(arabic), numeral)

    def test_1(self):
        self.assertEqual(roman_numerals.numeral(1), 'I')

    def test_2(self):
        self.assertEqual(roman_numerals.numeral(2), 'II')

    def test_3(self):
        self.assertEqual(roman_numerals.numeral(3), 'III')

    def test_4(self):
        self.assertEqual(roman_numerals.numeral(4), 'IV')

    def test_5(self):
        self.assertEqual(roman_numerals.numeral(5), 'V')

    def test_6(self):
        self.assertEqual(roman_numerals.numeral(6), 'VI')

    def test_9(self):
        self.assertEqual(roman_numerals.numeral(9), 'IX')

    def test_27(self):
        self.assertEqual(roman_numerals.numeral(27), 'XXVII')

    def test_48(self):
        self.assertEqual(roman_numerals.numeral(48), 'XLVIII')

    def test_59(self):
        self.assertEqual(roman_numerals.numeral(59), 'LIX')

    def test_87(self):
        self.assertEqual(roman_numerals.numeral(87), 'LXXXVII')

    def test_93(self):
        self.assertEqual(roman_numerals.numeral(93), 'XCIII')

    def test_141(self):
        self.assertEqual(roman_numerals.numeral(141), 'CXLI')

    def test_163(self):
        self.assertEqual(roman_numerals.numeral(163), 'CLXIII')

    def test_402(self):
        self.assertEqual(roman_numerals.numeral(402), 'CDII')

    def test_575(self):
        self.assertEqual(roman_numerals.numeral(575), 'DLXXV')

    def test_911(self):
        self.assertEqual(roman_numerals.numeral(911), 'CMXI')

    def test_1024(self):
        self.assertEqual(roman_numerals.numeral(1024), 'MXXIV')

    def test_3000(self):
            self.assertEqual(roman_numerals.numeral(3000), 'MMM')


if __name__ == '__main__':
    unittest.main()
