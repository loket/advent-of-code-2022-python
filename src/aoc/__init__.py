import itertools
import typing


def window(seq, n=2):
    """
    Returns a sliding window (of width n) over data from the iterable
    s -> (s0,s1,...s[n-1]), (s1,s2,...,sn), ...

    Stolen from: https://stackoverflow.com/a/6822773/6730769
    """
    it = iter(seq)
    result = tuple(itertools.islice(it, n))
    if len(result) == n:
        yield result
    for elem in it:
        result = result[1:] + (elem,)
        yield result


def solve(day: int, part: int, solution: typing.Callable[[str], typing.Union[str, int]]):
    with open(f"../../input/{str(day).zfill(2)}.txt", "r") as f:
        text = f.read()
        print(f"Part {part}:\n{solution(text)}")
