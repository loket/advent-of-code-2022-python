import typing


def solve(day: int, part_one: typing.Callable[[str], int], part_two: typing.Callable[[str], int]):
    with open(f"../../input/{str(day).zfill(2)}.txt", "r") as f:
        text = f.read()
        print(f"Part one: {part_one(text)}")
        print(f"Part two: {part_two(text)}")
