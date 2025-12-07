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
    for line in lines:
        jolts = [int(x) for x in line.strip()]
        d1 = max(jolts[:-1])
        d2 = max(jolts[jolts.index(d1) + 1 :])
        total += int(f"{d1}{d2}")

    return total


def get_jolts(jolts: list[int], remaining_jolts: list[int], remaining_length: int):
    if remaining_length == 1:
        jolts.append(max(remaining_jolts))
        return int("".join(jolts))
    d = max(remaining_jolts[: -remaining_length + 1])
    jolts.append(d)
    remaining_jolts = remaining_jolts[remaining_jolts.index(d) + 1 :]
    return get_jolts(jolts, remaining_jolts, remaining_length - 1)


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
    for line in lines:
        jolts = list(line.strip())
        total += get_jolts([], jolts, 12)

    return total


if __name__ == "__main__":
    print(part_one("aoc/inputs/day_03.txt"))
    print(part_two("aoc/inputs/day_03.txt"))
