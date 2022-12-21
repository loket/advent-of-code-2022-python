import typing

from src.aoc import solve


def parse_instructions(text: str) -> typing.Dict[str, typing.Union[int, typing.Tuple[str, str, str]]]:
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


class Day21:
    @staticmethod
    def part_one(text: str) -> typing.Optional[int]:
        instructions = parse_instructions(text)
        result = perform_instruction(instructions, "root")
        return result

    @staticmethod
    def part_two(text: str) -> typing.Optional[int]:
        return None


if __name__ == '__main__':
    solve(21, 1, Day21.part_one)
    solve(21, 2, Day21.part_two)
