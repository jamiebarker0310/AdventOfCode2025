import math

def part_one(file_path: str):
    """[summary]

    Args:
        file_path (str): [description]

    Returns:
        [type]: [description]
    """

    # read file
    with open(file_path) as f:
        lines = f.readlines()
    
    grid = [[x for x in line.split(" ") if x.strip()!=""] for line in lines]
    total = 0
    for j in range(len(grid[0])):
        digits = [int(grid[i][j]) for i in range(len(grid)-1)]
        if grid[-1][j] == "+":
            total += sum(digits)
        else:
            total += math.prod(digits)

    return total


def part_two(file_path: str):
    """[summary]

    Args:
        file_path (str): [description]

    Returns:
        [type]: [description]
    """

    with open(file_path) as f:
        lines = f.readlines()

    lines = [line.replace("\n", "") for line in lines]
    digits = []
    total = 0
    for j in range(len(lines[0])):
        column = "".join([lines[i][-j-1].strip() for i in range(len(lines)-1)])

        if column:
            digit = int(column)
            digits.append(int("".join(column)))
        operation = lines[-1][-j-1]

        if operation.strip():
            if operation == "+":
                total += sum(digits)
                digits = []
            else:
                total += math.prod(digits)
                digits = []

    return total


if __name__ == "__main__":
    print(part_one("aoc/inputs/day_06.txt"))
    print(part_two("aoc/inputs/day_06.txt"))