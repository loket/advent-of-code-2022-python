import typing
from typing import Any, Generator, List

from src.aoc import solve


def assignment_pair(text: str) -> list[list[int]]:
    """
    >>> assignment_pair("2-4,6-8")
    [[2, 3, 4], [6, 7, 8]]
    """
    pair_str = text.split(",")
    assignment_str = [p.split("-") for p in pair_str]
    return [list(range(int(a), int(b) + 1)) for a, b in assignment_str]


def is_fully_contained(a: list[int], b: list[int]) -> bool:
    a_in_b = all(n in b for n in a)
    b_in_a = all(n in a for n in b)
    return a_in_b or b_in_a


def is_partially_contained(a: list[int], b: list[int]) -> bool:
    a_in_b = any(n in b for n in a)
    b_in_a = any(n in a for n in b)
    return a_in_b or b_in_a


class Day04:
    @staticmethod
    def part_one(text: str) -> typing.Optional[int]:
        pairs = [assignment_pair(line) for line in text.splitlines()]
        return sum(is_fully_contained(a, b) for a, b in pairs)

    @staticmethod
    def part_two(text: str) -> typing.Optional[int]:
        pairs = [assignment_pair(line) for line in text.splitlines()]
        return sum(is_partially_contained(a, b) for a, b in pairs)


if __name__ == '__main__':
    solve(4, 1, Day04.part_one)
    solve(4, 2, Day04.part_two)
