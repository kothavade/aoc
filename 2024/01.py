from aocd import data
from collections import Counter


def split(data):
    l1 = []
    l2 = []
    for line in data.split("\n"):
        a, b = line.split("   ")
        l1.append(int(a))
        l2.append(int(b))
    return (l1, l2)


def part1(data):
    l1, l2 = split(data)
    res = sum(abs(a - b) for a, b in zip(sorted(l1), sorted(l2)))
    print(res)


def part2(data):
    l1, l2 = split(data)
    ctr = Counter(l2)
    res = sum(n * ctr.get(n, 0) for n in l1)
    print(res)


if __name__ == "__main__":
    part1(data)
    part2(data)
