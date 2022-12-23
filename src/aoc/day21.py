import typing

from src.aoc import solve


def parse_instructions(text: str) -> typing.Dict[
    str, typing.Union[int, typing.Tuple[str, str, str], typing.Callable[[], typing.Generator[int, None, None]]]
]:
    instructions = dict()
    for line in text.splitlines():
        left = line[0:4]
        right = line[6:]
        if str(right).isnumeric():
            instructions[left] = int(right)
        else:
            a, operation, b = right.split(" ")
            instructions[left] = a, operation, b
    return instructions


def perform_instruction(
    instructions: typing.Dict[str, typing.Union[int, typing.Tuple[str, str, str]]],
    instruction: str
) -> int:
    match = instructions[instruction]
    if isinstance(match, int):
        return match
    if callable(match):
        return next(match())
    a, operation, b = match
    a_result = perform_instruction(instructions, a)
    b_result = perform_instruction(instructions, b)
    if operation == "-":
        return a_result - b_result
    if operation == "+":
        return a_result + b_result
    if operation == "*":
        return a_result * b_result
    if operation == "/":
        return int(a_result / b_result)
    raise RuntimeError(f"Unsupported operation: {operation}")


def perform_instructions_until_match_part_two(
    instructions: typing.Dict[
        str, typing.Union[int, typing.Tuple[str, str, str], typing.Callable[[], typing.Generator[int, None, None]]]
    ],
):
    global humn_increment
    root_a, _, root_b = instructions["root"]
    results_match = False
    while not results_match:
        result_a = perform_instruction(instructions, root_a)
        result_b = perform_instruction(instructions, root_b)
        diff = result_a - result_b
        humn_increment = int(diff / 100)
        if humn_increment == 0:
            humn_increment = 1
        if result_a == result_b:
            results_match = True


humn_counter = 0
humn_increment = 1


def humn() -> typing.Generator[int, None, None]:
    global humn_counter, humn_increment
    while True:
        humn_counter += humn_increment
        yield humn_counter


class Day21:
    @staticmethod
    def part_one(text: str) -> typing.Optional[int]:
        instructions = parse_instructions(text)
        result = perform_instruction(instructions, "root")
        return result

    @staticmethod
    def part_two(text: str) -> typing.Optional[int]:
        instructions = parse_instructions(text)
        # Override "humn"
        instructions["humn"] = humn
        # I can't be bothered, so I'll be brute forcing this thing
        perform_instructions_until_match_part_two(instructions)
        result = next(humn()) - 1
        return result


if __name__ == '__main__':
    solve(21, 1, Day21.part_one)
    solve(21, 2, Day21.part_two)
