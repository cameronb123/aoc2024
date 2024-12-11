from pathlib import Path


def get_routes_from_current(current_coordinates: tuple[int, int], grid: list[list[int]]) -> tuple[set[int], int]:
    x, y = current_coordinates
    targets = set()
    trails = 0
    current_value = grid[x][y]

    for i, j in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        if 0 <= x + i < len(grid) and 0 <= y + j < len(grid[0]):
            if grid[x + i][y + j] == current_value + 1:
                if grid[x + i][y + j] == 9:
                    targets.add((x + i, y + j))
                    trails += 1
                else:
                    new_targets, new_trails = get_routes_from_current((x + i, y + j), grid)
                    targets.update(new_targets)
                    trails += new_trails
    return targets, trails


def solution(file: Path) -> tuple[int, int]:
    with open(file) as f:
        input_values = f.read().split("\n")

        grid = [[int(i) if i != "." else -1 for i in row] for row in input_values]
        target_count = 0
        trail_count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    new_targets, new_trail_count = get_routes_from_current((i, j), grid)
                    target_count += len(new_targets)
                    trail_count += new_trail_count

    return target_count, trail_count


if __name__ == "__main__":
    test_file = Path(__file__).parent / "test.txt"
    input_file = Path(__file__).parent / "input.txt"
    test_1, test_2 = solution(test_file)
    assert test_1 == 36
    assert test_2 == 81
    part_1, part_2 = solution(input_file)
    print("Part 1:", part_1)
    print("Part 2:", part_2)
