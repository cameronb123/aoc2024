from pathlib import Path


def get_next_result(start: int, values: list[int], concat: bool = False) -> list[int]:
    results = [start * values[0], start + values[0]]
    if concat:
        results = [*results, int(str(start) + str(values[0]))]
    if values[1:]:
        new_results = []
        for result in results:
            new_results.extend(get_next_result(result, values[1:], concat))
        results = new_results
    return results


def solution(file: Path) -> tuple[int, int]:
    with open(file) as f:
        input_values = f.read().split("\n")

        sum = 0
        concat_sum = 0
        for row in input_values:
            values = row.split(": ")
            target = int(values[0])
            inputs = [int(v) for v in values[1].split(" ")]
            results = get_next_result(inputs[0], inputs[1:])
            if target in results:
                sum += target
            concat_results = get_next_result(inputs[0], inputs[1:], True)
            if target in concat_results:
                concat_sum += target

    return sum, concat_sum


if __name__ == "__main__":
    test_file = Path(__file__).parent / "test.txt"
    input_file = Path(__file__).parent / "input.txt"
    test_1, test_2 = solution(test_file)
    assert test_1 == 3749
    assert test_2 == 11387
    part_1, part_2 = solution(input_file)
    print("Part 1:", part_1)
    print("Part 2:", part_2)
