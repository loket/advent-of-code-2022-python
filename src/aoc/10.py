import typing

from src.aoc import solve

small_example = """noop
addx 3
addx -5"""

large_example = """addx 15
addx -11
addx 6
addx -3
addx 5
addx -1
addx -8
addx 13
addx 4
noop
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx -35
addx 1
addx 24
addx -19
addx 1
addx 16
addx -11
noop
noop
addx 21
addx -15
noop
noop
addx -3
addx 9
addx 1
addx -3
addx 8
addx 1
addx 5
noop
noop
noop
noop
noop
addx -36
noop
addx 1
addx 7
noop
noop
noop
addx 2
addx 6
noop
noop
noop
noop
noop
addx 1
noop
noop
addx 7
addx 1
noop
addx -13
addx 13
addx 7
noop
addx 1
addx -33
noop
noop
noop
addx 2
noop
noop
noop
addx 8
noop
addx -1
addx 2
addx 1
noop
addx 17
addx -9
addx 1
addx 1
addx -3
addx 11
noop
noop
addx 1
noop
addx 1
noop
noop
addx -13
addx -19
addx 1
addx 3
addx 26
addx -30
addx 12
addx -1
addx 3
addx 1
noop
noop
noop
addx -9
addx 18
addx 1
addx 2
noop
noop
addx 9
noop
noop
noop
addx -1
addx 2
addx -37
addx 1
addx 3
noop
addx 15
addx -21
addx 22
addx -6
addx 1
noop
addx 2
addx 1
noop
addx -10
noop
noop
addx 20
addx 1
addx 2
addx 2
addx -6
addx -11
noop
noop
noop
"""


def noop(_c: int, _x: int) -> typing.Iterable[typing.Tuple[int, int]]:
    yield _c + 1, _x


def addx(_c: int, _x: int, _y: int) -> typing.Iterable[typing.Tuple[int, int]]:
    yield _c + 1, _x
    yield _c + 2, _x + _y


def map_command(_c: int, _x: int, text: str) -> typing.Iterable[typing.Tuple[int, int]]:
    if text.startswith("noop"):
        return noop(_c, _x)
    if text.startswith("addx"):
        y = int(text.split(' ')[1])
        return addx(_c, _x, y)
    raise RuntimeError("Unsupporded command: " + text)


def cycles(text: str) -> typing.Iterable[typing.Tuple[int, int]]:
    c, x = 1, 1
    for line in text.splitlines():
        command = map_command(c, x, line)
        for ci, xi in command:
            c, x = ci, xi
            yield c, x


def part_one(text: str) -> int:
    """
    >>> part_one(large_example)
    13140
    """
    every_40 = list(cycles(text))[18::40]
    signal_strengths = [c * x for c, x in every_40]
    return sum(signal_strengths)


def part_two(text: str) -> int:
    raise NotImplementedError


if __name__ == '__main__':
    solve(10, part_one, part_two)
