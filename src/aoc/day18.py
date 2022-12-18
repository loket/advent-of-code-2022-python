import typing

from src.aoc import solve


def count_connected(cube: typing.Tuple[int, int, int], cubes: typing.Iterable[typing.Tuple[int, int, int]]) -> int:
    """
    >>> c = [(1,1,1), (2,1,1)]
    >>> count_connected((1,1,1), c)
    1
    """
    x, y, z = cube
    cubes_excluding = set(cubes).difference({cube})
    xy_matches = sum(c[0] == x and c[1] == y and abs(c[2] - z) == 1 for c in cubes_excluding)
    xz_matches = sum(c[0] == x and c[2] == z and abs(c[1] - y) == 1 for c in cubes_excluding)
    yz_matches = sum(c[1] == y and c[2] == z and abs(c[0] - x) == 1 for c in cubes_excluding)
    return sum([xy_matches, xz_matches, yz_matches])


def surface_area(cubes: typing.Iterable[typing.Tuple[int, int, int]]) -> int:
    """
    >>> c = [(1,1,1), (2,1,1)]
    >>> surface_area(c)
    10
    """
    connected = [count_connected(cube, cubes) for cube in cubes]
    return sum(6 - c for c in connected)


def parse_tuple(text: str) -> typing.Tuple[int, int, int]:
    s = text.split(",")
    return int(s[0]), int(s[1]), int(s[2])


class Day18:
    @staticmethod
    def part_one(text: str) -> typing.Optional[int]:
        cubes = [parse_tuple(line) for line in text.splitlines()]
        return surface_area(cubes)

    @staticmethod
    def part_two(text: str) -> typing.Optional[int]:
        return None


if __name__ == '__main__':
    solve(18, 1, Day18.part_one)
    solve(18, 2, Day18.part_two)
