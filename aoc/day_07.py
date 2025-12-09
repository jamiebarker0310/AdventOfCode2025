from collections import Counter


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

    start = None
    splitters = set()
    for j, line in enumerate(lines):
        for i, char in enumerate(line.strip()):
            if char == "S":
                start = i - j * 1j
            elif char == "^":
                splitters.add(i - j * 1j)
    count = 0
    beams = set([start])
    for _ in range(len(lines)):
        new_beams = set()
        for beam in beams:
            beam -= 1j
            if beam in splitters:
                new_beams.add(beam + 1)
                new_beams.add(beam - 1)
                count += 1
            else:
                new_beams.add(beam)
        beams = new_beams

    return count


def part_two(file_path: str):
    """[summary]

    Args:
        file_path (str): [description]

    Returns:
        [type]: [description]
    """

    with open(file_path) as f:
        lines = f.readlines()

    start = None
    splitters = set()
    for j, line in enumerate(lines):
        for i, char in enumerate(line):
            if char == "S":
                start = i - j * 1j
            elif char == "^":
                splitters.add(i - j * 1j)

    count = 0
    beams = Counter([start])
    for _ in range(len(lines)):
        new_beams = Counter()
        for beam, count in beams.items():
            beam -= 1j
            if beam in splitters:
                new_beams[beam + 1] += count
                new_beams[beam - 1] += count
            else:
                new_beams[beam] += count
        beams = new_beams

    return beams.total()


if __name__ == "__main__":
    print(part_one("aoc/inputs/day_07.txt"))
    print(part_two("aoc/inputs/day_07.txt"))
