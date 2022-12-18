from unittest import TestCase
from src.aoc.day18 import Day18


class TestDay18(TestCase):
    input = """2,2,2
1,2,2
3,2,2
2,1,2
2,3,2
2,2,1
2,2,3
2,2,4
2,2,6
1,2,5
3,2,5
2,1,5
2,3,5"""

    def test_part_one(self):
        result = Day18.part_one(self.input)
        self.assertEqual(result, 64)

    def test_part_two(self):
        result = Day18.part_two(self.input)
        self.assertEqual(result, None)
