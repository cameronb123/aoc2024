import re
from pathlib import Path


def solution(file: Path) -> tuple[int, int]:
    with open(file) as f:
        input_values = f.read()

    multipliers = re.findall(r"mul\((\d{1,3},\d{1,3})\)", input_values)
    all_commands = re.findall(r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)", input_values)

    sum = 0
    for multiplier in multipliers:
        a, b = multiplier.split(",")
        sum += int(a) * int(b)

    multiply = True
    enabled_sum = 0
    for command in all_commands:
        if command == "do()":
            multiply = True
        elif command == "don't()":
            multiply = False
        elif multiply:
            multiplier = re.match(r"mul\((\d{1,3},\d{1,3})\)", command).group(1)
            a, b = multiplier.split(",")
            enabled_sum += int(a) * int(b)

    return sum, enabled_sum


if __name__ == "__main__":
    test_file = Path(__file__).parent / "test.txt"
    input_file = Path(__file__).parent / "input.txt"
    test_1, test_2 = solution(test_file)
    assert test_1 == 161
    assert test_2 == 48
    part_1, part_2 = solution(input_file)
    print("Part 1:", part_1)
    print("Part 2:", part_2)
