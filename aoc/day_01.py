import os

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
    pos = 50
    count = 0
    for rotation in lines:
        sign = 1
        if rotation[0]=="L":
            sign *= -1
        pos += int(rotation[1:]) * sign
        pos %= 100

        if pos == 0:
            count += 1

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
    
    pos = 50
    count = 0
    for rotation in lines:
        on_click = (pos%100 == 0)
        sign = 1
        if rotation[0]=="L":
            sign *= -1
        pos += int(rotation[1:]) * sign

        if pos >= 100:
            count += pos // 100
        
        if pos <= 0:
            count += (abs(pos) // 100) + 1
            if on_click:
                count -= 1
        
        pos %= 100

    return count


if __name__ == "__main__":
    print(part_one("aoc/inputs/day_01.txt"))
    print(part_two("aoc/inputs/day_01.txt"))
