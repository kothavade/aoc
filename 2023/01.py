from aocd import data
import timeit
import re


def get_first_last_num(line):
    m = re.findall(r"\d", line)
    return int(m[0] + m[-1])


def part1(data):
    res = sum(get_first_last_num(line) for line in data.split("\n"))
    return res


map = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


# brute force
def part2_brute(data):
    res = 0
    for l in data.split("\n"):
        first, last = "", ""
        for i in range(len(l)):
            # if num
            if l[i].isdigit():
                if not first:
                    first = l[i]
                last = l[i]
                continue
            # if num word
            for k, v in map.items():
                if l[i : i + len(k)] == k:
                    if not first:
                        first = v
                    last = v
                    break
        res += int(first + last)
    return res


nums = r"(one|two|three|four|five|six|seven|eight|nine|\d)"


def get_num(a: str, b: str):
    return int((a if a.isdigit() else map[a]) + (b if b.isdigit() else map[b]))


# regex lookahead, per:
# https://www.reddit.com/r/adventofcode/comments/1884fpl/2023_day_1for_those_who_stuck_on_part_2/kbjy6ey/
# get all matches and parse
def part2_re(data):
    rgx = re.compile(rf"(?={nums})")
    res = 0
    for l in data.split("\n"):
        m = rgx.findall(l)
        res += get_num(m[0], m[-1])
    return res


# optimized, only get first and last match
def part2_re_opt(data):
    rgx = re.compile(rf"(?={nums}).*{nums}")
    res = 0
    for l in data.split("\n"):
        m = rgx.search(l)
        res += get_num(m.group(1), m.group(2))
    return res


if __name__ == "__main__":
    #     data = """1abc2
    # pqr3stu8vwx
    # a1b2c3d4e5f
    # treb7uchet"""
    #     data = """two1nine
    # eightwothree
    # abcone2threexyz
    # xtwone3four
    # 4nineeightseven2
    # zoneight234
    # 7pqrstsixteen"""

    print(part1(data))
    # print(part2_brute(data))
    # print(part2_re(data))
    print(part2_re_opt(data))
    print(timeit.timeit(lambda: part2_brute(data), number=100))
    print(timeit.timeit(lambda: part2_re(data), number=100))
    print(timeit.timeit(lambda: part2_re_opt(data), number=100))
    # 1.373984833015129
    # 0.15429012500680983
    # 0.08888662490062416
