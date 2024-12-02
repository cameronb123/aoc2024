from pathlib import Path


def solution(file: Path) -> tuple[int, int]:
    with open(file) as f:
        input_values = f.read().split("\n")

        left_list = []
        right_list = []
        for row in input_values:
            left, right = row.split("   ")
            left_list.append(left)
            right_list.append(right)

        left_list.sort()
        right_list.sort()

        distance = 0
        for i in range(len(left_list)):
            distance += abs(int(left_list[i]) - int(right_list[i]))

        count_dict = {}
        for i in right_list:
            count_dict[i] = count_dict.get(i, 0) + 1

        similarity = 0
        for i in left_list:
            similarity += int(i) * count_dict.get(i, 0)

    return distance, similarity


if __name__ == "__main__":
    test_file = Path(__file__).parent / "test.txt"
    input_file = Path(__file__).parent / "input.txt"
    test_1, test_2 = solution(test_file)
    assert test_1 == 11
    assert test_2 == 31
    part_1, part_2 = solution(input_file)
    print("Part 1:", part_1)
    print("Part 2:", part_2)
