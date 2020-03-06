import unittest

from src.parser import parse_phone_number


class ParserTestCase(unittest.TestCase):

    def test_parse_phone_number(self):
        self.assertEqual(parse_phone_number("87473134455"), 77473134455)
        self.assertEqual(parse_phone_number("Осыларды сатамын. Тел 8 747 313 44 55"), 77473134455)
        self.assertEqual(parse_phone_number("Жер орын сатылады. Тел 747 313 44 55"), 77473134455)
        self.assertEqual(parse_phone_number("SSD диск сатылады. Тел +7(747)313-44-55. Жақсы жағдайда"), 77473134455)


if __name__ == "__main__":
    unittest.main()
