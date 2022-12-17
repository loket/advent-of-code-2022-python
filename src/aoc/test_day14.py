from unittest import TestCase
from src.aoc.day14 import Day14


class TestDay14(TestCase):
    input = """498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9
"""

    def test_part_one(self):
        result = Day14.part_one(self.input)
        self.assertEqual(result, 24)

    def test_part_two(self):
        result = Day14.part_two(self.input)
        self.assertEqual(result, None)
