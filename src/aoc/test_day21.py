from unittest import TestCase
from src.aoc.day21 import Day21


class TestDay21(TestCase):
    input = """root: pppw + sjmn
dbpl: 5
cczh: sllz + lgvd
zczc: 2
ptdq: humn - dvpt
dvpt: 3
lfqf: 4
humn: 5
ljgn: 2
sjmn: drzm * dbpl
sllz: 4
pppw: cczh / lfqf
lgvd: ljgn * ptdq
drzm: hmdt - zczc
hmdt: 32"""

    def test_part_one(self):
        result = Day21.part_one(self.input)
        self.assertEqual(result, 152)

    def test_part_two(self):
        result = Day21.part_two(self.input)
        self.assertEqual(result, None)
