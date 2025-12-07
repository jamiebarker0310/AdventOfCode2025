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

    grid = {}
    for y, line in enumerate(lines):
        for x, char in enumerate(line.strip()):
            grid[x + (y * 1j)] = char == "@"

    count = 0
    for key, value in grid.items():
        if not value:
            continue
        neighbours = 0
        for x in [-1, 0, 1]:
            for y in [-1j, 0, 1j]:
                if x == 0 and y == 0:
                    pass
                elif grid.get(key + x + y, False):
                    neighbours += 1
        if neighbours < 4:
            count += 1

    return count


def grid_iteration(grid):
    removable = []
    for key, value in grid.items():
        if not value:
            continue
        neighbours = 0
        for x in [-1, 0, 1]:
            for y in [-1j, 0, 1j]:
                if x == 0 and y == 0:
                    pass
                elif grid.get(key + x + y, False):
                    neighbours += 1
        if neighbours < 4:
            removable.append(key)

    for pos in removable:
        grid[pos] = False

    return grid, len(removable)


def part_two(file_path: str):
    """[summary]

    Args:
        file_path (str): [description]

    Returns:
        [type]: [description]
    """

    with open(file_path) as f:
        lines = f.readlines()

    grid = {}
    for y, line in enumerate(lines):
        for x, char in enumerate(line.strip()):
            grid[x + (y * 1j)] = char == "@"

    removed = 1
    total = 0
    while removed:
        grid, removed = grid_iteration(grid)
        total += removed

    return total


if __name__ == "__main__":
    print(part_one("aoc/inputs/day_04.txt"))
    print(part_two("aoc/inputs/day_04.txt"))
