from unittest import TestCase
from src.aoc.day04 import Day04


class TestDay04(TestCase):
    input = """2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8"""

    def test_part_one(self):
        result = Day04.part_one(self.input)
        self.assertEqual(result, 2)

    def test_part_two(self):
        result = Day04.part_two(self.input)
        self.assertEqual(result, 4)
