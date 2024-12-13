from pathlib import Path


def get_bigger_nums(rules: dict[int, list[int]]) -> dict[int, list[int]]:
    """Get a dictionary mapping a number to all the numbers that it's bigger than."""
    bigger_nums = {}
    for rule in rules:
        for value in rules[rule]:
            bigger_nums[value] = [*bigger_nums.get(value, []), rule]
    return bigger_nums


def solution(file: Path) -> tuple[int, int]:
    with open(file) as f:
        input_values = f.read().split("\n")

        rules: dict[int, list[int]] = {}
        updates: list[list[int]] = []

        rows = iter(input_values)
        row = next(rows)
        while row:
            if row == "":
                break
            rule, value = row.split("|")
            rules[int(rule)] = [*rules.get(int(rule), []), int(value)]
            row = next(rows, None)
        row = next(rows)
        while row:
            updates.append([int(x) for x in row.split(",")])
            row = next(rows, None)

        bigger_nums_dict = get_bigger_nums(rules)

        mid_pages = 0
        fixed_mid_pages = 0
        unsuccessfuls = []
        for update in updates:
            successful = True
            for i, page in enumerate(update):
                # Check if the remaining pages are all bigger nums
                remaining_pages = update[i + 1:]
                if any(remaining_page in bigger_nums_dict.get(page, []) for remaining_page in remaining_pages):
                    successful = False
                    unsuccessfuls.append(update)
                    break
            if successful:
                mid_pages += update[len(update) // 2]

        for update in unsuccessfuls:
            # Order correctly using the rules
            sorted_update = []
            for i, page in enumerate(update):
                if i == 0:
                    sorted_update.append(page)
                else:
                    bigger_nums = bigger_nums_dict.get(page, [])
                    index = 0
                    while index < len(sorted_update):
                        if sorted_update[index] in bigger_nums:
                            break
                        index += 1
                    sorted_update.insert(index, page)
            fixed_mid_pages += sorted_update[len(sorted_update) // 2]

    return mid_pages, fixed_mid_pages


if __name__ == "__main__":
    test_file = Path(__file__).parent / "test.txt"
    input_file = Path(__file__).parent / "input.txt"
    test_1, test_2 = solution(test_file)
    assert test_1 == 143
    assert test_2 == 123
    part_1, part_2 = solution(input_file)
    print("Part 1:", part_1)
    print("Part 2:", part_2)
