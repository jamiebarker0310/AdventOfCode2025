from collections import defaultdict
import heapq
from itertools import combinations
import math

def get_circuit(node, graph, circuit):

    for neighbour in graph[node]:
        if neighbour not in circuit:
            circuit.add(neighbour)
            circuit = get_circuit(neighbour, graph, circuit)
    return circuit

def part_one(file_path: str, n=1000):
    """[summary]

    Args:
        file_path (str): [description]

    Returns:
        [type]: [description]
    """

    # read file
    with open(file_path) as f:
        lines = f.readlines()
    
    boxes = [tuple(int(x) for x in line.split(",")) for line in lines]

    distances = {}
    for i, b1 in enumerate(boxes[:-1]):
        for b2 in boxes[i+1:]:
            dist = sum((p1 - p2)**2 for p1, p2 in zip(b1, b2))
            distances[(b1,b2)] = dist

    edges = heapq.nsmallest(n, combinations(boxes,2), key=lambda x: sum((p1 - p2)**2 for p1, p2 in zip(x[0], x[1])))

    graph = defaultdict(set)
    for n1, n2 in edges:
        graph[n1].add(n2)
        graph[n2].add(n1)

    circuits = set(tuple(sorted(get_circuit(node, graph, set()))) for node in graph)

    return math.prod(heapq.nlargest(3, map(len, circuits)))


def part_two(file_path: str):
    """[summary]

    Args:
        file_path (str): [description]

    Returns:
        [type]: [description]
    """

    with open(file_path) as f:
        lines = f.readlines()
    
    boxes = [tuple(int(x) for x in line.split(",")) for line in lines]

    distances = {}
    for i, b1 in enumerate(boxes[:-1]):
        for b2 in boxes[i+1:]:
            dist = sum((p1 - p2)**2 for p1, p2 in zip(b1, b2))
            distances[(b1,b2)] = dist

    ordered_edges = sorted(distances.keys(), key=distances.get)

    graph = defaultdict(set)
    i = 0
    while len(get_circuit(boxes[0], graph, set())) < len(boxes):
        n1, n2 = ordered_edges[i]
        graph[n1].add(n2)
        graph[n2].add(n1)
        i += 1

    return n1[0] * n2[0]


if __name__ == "__main__":
    print(part_one("aoc/inputs/day_08.txt"))
    print(part_two("aoc/inputs/day_08.txt"))