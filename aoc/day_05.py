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


    ranges = lines[:lines.index("\n")]
    ids = [int(x) for x in lines[lines.index("\n")+1:]]

    ranges = [[int(x) for x in r.split("-")] for r in ranges]

    count = 0
    for id in ids:
        for a,b in ranges:
            if id >= a and id <= b:
                count += 1
                break

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

    ranges = lines[:lines.index("\n")]
    ranges = [[int(x) for x in r.split("-")] for r in ranges]

    count = 0
    for i in range(len(ranges)):
        a, b = ranges[i]
        distinct = True
        for j in range(i+1, len(ranges)):
            c, d = ranges[j]
            if (b < c) or (d < a):
                continue
            else:
                distinct = False
                new_range = [min(a,c), max(b,d)]
                ranges[j] = new_range
                break
        if distinct:
            count += b  -a +1
    
    return count


if __name__ == "__main__":
    print(part_one("aoc/inputs/day_05.txt"))
    print(part_two("aoc/inputs/day_05.txt"))