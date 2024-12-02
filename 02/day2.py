from pathlib import Path


def is_safe(levels: list[int]) -> bool:
    if not (list(sorted(levels)) == levels or list(sorted(levels, reverse=True)) == levels):
        # Levels are not ascending or descending
        return False

    diff_array = [0 < abs(levels[j] - levels[j - 1]) < 4 for j in range(1, len(levels))]
    if not all(diff_array):
        return False

    return True


def solution(file: Path) -> tuple[int, int]:
    with open(file) as f:
        input_values = f.read().split("\n")

        safe_rows = 0
        problem_levels = []

        for row in input_values:
            levels = [int(i) for i in row.split(" ")]

            if is_safe(levels):
                safe_rows += 1
            else:
                problem_levels.append(levels)

        additional_safe_rows = 0
        for levels in problem_levels:
            for i in range(len(levels)):
                modified_levels = levels[:i] + levels[i+1:]
                if is_safe(modified_levels):
                    additional_safe_rows += 1
                    break

    return safe_rows, safe_rows + additional_safe_rows


if __name__ == "__main__":
    test_file = Path(__file__).parent / "test.txt"
    input_file = Path(__file__).parent / "input.txt"
    test_1, test_2 = solution(test_file)
    assert test_1 == 2
    assert test_2 == 4
    part_1, part_2 = solution(input_file)
    print("Part 1:", part_1)
    print("Part 2:", part_2)
