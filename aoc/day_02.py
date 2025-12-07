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

    total = 0
    for a, b in [x.strip().split("-") for x in lines[0].split(",")]:
        for i in range(int(a), int(b) + 1):
            i_str = str(i)
            if i_str[: len(i_str) // 2] == i_str[len(i_str) // 2 :]:
                total += i
    return total


def _is_invalid(i_str, line):
    if len(i_str) % line != 0:
        return False

    init_i_str = i_str[:line]
    for k in range(line, len(i_str), line):
        if i_str[k : k + line] != init_i_str:
            return False
    return True


def part_two(file_path: str):
    """[summary]

    Args:
        file_path (str): [description]

    Returns:
        [type]: [description]
    """

    with open(file_path) as f:
        lines = f.readlines()

    total = 0
    for a, b in [x.strip().split("-") for x in lines[0].split(",")]:
        for i in range(int(a), int(b) + 1):
            i_str = str(i)
            for j in range(1, len(i_str) // 2 + 1):
                if _is_invalid(i_str, j):
                    total += i
                    break

    return total


if __name__ == "__main__":
    print(part_one("aoc/inputs/day_02.txt"))
    print(part_two("aoc/inputs/day_02.txt"))
