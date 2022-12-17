import itertools
import typing

from src.aoc import solve, window


def ranges(text: str) -> typing.Iterable[typing.Tuple[int, int]]:
    """
    >>> t = "498,4 -> 498,6 -> 496,6"
    >>> p = sorted(set(ranges(t)))
    >>> p
    [(496, 6), (497, 6), (498, 4), (498, 5), (498, 6)]
    """
    points_str = [point.split(",")[:2] for point in text.split(" -> ")]
    points = ((int(x), int(y)) for x, y in points_str)
    # Split points into sliding windows (pairs)
    for win in window(points, n=2):
        # Get both x/y coordinates, and sort them
        # (otherwise, the range function below will not work)
        xs = sorted([win[0][0], win[1][0]])
        ys = sorted([win[0][1], win[1][1]])
        xr = range(xs[0], xs[1] + 1)
        yr = range(ys[0], ys[1] + 1)
        # Return the Cartesian product of the coordinates
        for pair in itertools.product(xr, yr):
            yield pair


def full_of_sand(
    grains: typing.Iterable[typing.Tuple[int, int]],
    rocks: typing.Iterable[typing.Tuple[int, int]],
) -> bool:
    # TODO: Check width/height of rocks, to find boundaries
    return (500, 1) in grains


def combine(
    grains: typing.Set[typing.Tuple[int, int]],
    rocks: typing.Set[typing.Tuple[int, int]]
) -> typing.Set[typing.Tuple[int, int]]:
    return grains.union(rocks)


def something_below(
    grain: typing.Tuple[int, int],
    grains: typing.Set[typing.Tuple[int, int]],
    rocks: typing.Set[typing.Tuple[int, int]]
) -> bool:
    everything = list(combine(grains, rocks))
    return (grain[0], grain[1] + 1) in everything


def something_below_to_the_left(
    grain: typing.Tuple[int, int],
    grains: typing.Set[typing.Tuple[int, int]],
    rocks: typing.Set[typing.Tuple[int, int]]
) -> bool:
    everything = combine(grains, rocks)
    return (grain[0] - 1, grain[1] + 1) in everything


def something_below_to_the_right(
    grain: typing.Tuple[int, int],
    grains: typing.Set[typing.Tuple[int, int]],
    rocks: typing.Set[typing.Tuple[int, int]]
) -> bool:
    everything = combine(grains, rocks)
    return (grain[0] + 1, grain[1] + 1) in everything


def find_bounds(
    rocks: typing.Iterable[typing.Tuple[int, int]]
) -> typing.Tuple[typing.Tuple[int, int], typing.Tuple[int, int]]:
    min_x = min(x for x, _ in rocks)
    max_x = max(x for x, _ in rocks)
    min_y = min(y for _, y in rocks)
    max_y = max(y for _, y in rocks)
    return (min_x, min_y), (max_x, max_y)


def in_bounds(
    grain: typing.Tuple[int, int],
    bounds: typing.Tuple[typing.Tuple[int, int], typing.Tuple[int, int]]
) -> bool:
    (min_x, min_y), (max_x, max_y) = bounds
    x, y = grain
    return min_x <= x <= max_x or 0 <= y <= max_y


def scan_rocks(text: str) -> int:
    rocks = []
    for line in text.splitlines():
        for r in ranges(line):
            rocks.append(r)
    # rocks = {r for r in [ranges(line) for line in text.splitlines()]}
    grains_at_rest = []
    bounds = find_bounds(rocks)
    # while not full_of_sand(grains_at_rest, rocks):
    out_of_bounds = False
    while not out_of_bounds:
        grains_set = set(grains_at_rest)
        rocks_set = set(rocks)
        grain = (500, 0)
        while grain not in grains_at_rest:
            if not in_bounds(grain, bounds):
                out_of_bounds = True
                break
            if not something_below(grain, grains_set, rocks_set):
                grain = grain[0], grain[1] + 1
                continue
            if not something_below_to_the_left(grain, grains_set, rocks_set):
                grain = grain[0] - 1, grain[1] + 1
                continue
            if not something_below_to_the_right(grain, grains_set, rocks_set):
                grain = grain[0] + 1, grain[1] + 1
                continue
            # If you've made it this far, it means the sand grain is at rest
            grains_at_rest.append(grain)
    return len(grains_at_rest)


class Day14:
    @staticmethod
    def part_one(text: str) -> typing.Optional[int]:
        return scan_rocks(text)

    @staticmethod
    def part_two(text: str) -> typing.Optional[int]:
        return None


if __name__ == '__main__':
    solve(14, 1, Day14.part_one)
    solve(14, 2, Day14.part_two)
