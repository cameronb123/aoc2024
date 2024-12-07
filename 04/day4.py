from pathlib import Path


def check_diagonal_mas(input_values: list[str], start_i: int, start_j: int) -> bool:
    """Check for a diagonal 'MAS' which forms a cross with the current start coordinates.

    Only check right and below so that we don't double count crosses."""

    # Check the bottom left diagonal from the right
    i = start_i
    j = start_j + 2

    if "".join([input_values[i+k][j-k] for k in range(3) if i+k < len(input_values) and j-k >= 0]) in ("MAS", "SAM"):
        return True

    # Check the upper right diagonal from the bottom
    i = start_i + 2
    j = start_j

    if "".join([input_values[i-k][j+k] for k in range(3) if i-k >= 0 and j+k < len(input_values[i])]) in ("MAS", "SAM"):
        return True

    return False



def solution(file: Path) -> tuple[int, int]:
    with open(file) as f:
        input_values = f.read().split("\n")

        counts = 0
        mas_counts = 0

        # XMAS check
        for i in range(len(input_values)):
            for j in range(len(input_values[i])):
                current_letter = input_values[i][j]
                if current_letter == "X":
                    max_j = min(j + 4, len(input_values[i]))
                    max_i = min(i + 4, len(input_values))
                    min_j = max(j - 4, -1)
                    min_i = max(i - 4, -1)
                    # Check the row
                    if "".join(input_values[i][j:max_j]) == "XMAS":
                        counts += 1
                    # Check the row backwards
                    if "".join(input_values[i][min_j+1:j+1]) == "SAMX":
                        counts += 1
                    # Check the column
                    if "".join([input_values[k][j] for k in range(i, max_i)]) == "XMAS":
                        counts += 1
                    # Check the column backwards
                    if "".join([input_values[k][j] for k in range(min_i+1, i+1)]) == "SAMX":
                        counts += 1
                    # Check the diagonals
                    # Bottom right
                    if "".join([input_values[i+k][j+k] for k in range(4) if i+k < max_i and j+k < max_j]) == "XMAS":
                        counts += 1
                    # Bottom left
                    if "".join([input_values[i+k][j-k] for k in range(4) if i+k < max_i and j-k > min_j]) == "XMAS":
                        counts += 1
                    # Top right
                    if "".join([input_values[i-k][j+k] for k in range(4) if i-k > min_i and j+k < max_j]) == "XMAS":
                        counts += 1
                    # Top left
                    if "".join([input_values[i-k][j-k] for k in range(4) if i-k > min_i and j-k > min_j]) == "XMAS":
                        counts += 1

        # X-MAS check
        print("Checking X-MAS")
        for i in range(len(input_values)):
            for j in range(len(input_values[i])):
                current_letter = input_values[i][j]
                if current_letter in ("M", "S"):
                    max_j = min(j + 3, len(input_values[i]))
                    max_i = min(i + 3, len(input_values))
                    # Check the bottom right diagonal
                    if "".join([input_values[i+k][j+k] for k in range(3) if i+k < max_i and j+k < max_j]) in ("MAS", "SAM"):
                        if check_diagonal_mas(input_values, i, j):
                            mas_counts += 1

    return counts, mas_counts


if __name__ == "__main__":
    test_file = Path(__file__).parent / "test.txt"
    input_file = Path(__file__).parent / "input.txt"
    test_1, test_2 = solution(test_file)
    assert test_1 == 18
    assert test_2 == 9
    part_1, part_2 = solution(input_file)
    print("Part 1:", part_1)
    print("Part 2:", part_2)
