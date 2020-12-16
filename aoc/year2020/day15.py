# coding: utf8

from aoc import aoc


def rfind(iterable, item):
    for c, i in reversed(list(enumerate(iterable))):
        if i == item:
            return c

    return None


class Problem(aoc.Problem):
    def solve(self, part):

        if part == 1:
            upperbound = 2020
        else:
            upperbound = 30_000_000

        numbers = [int(n) for n in self.dataset.split(",")]
        last_spoken = {}
        for index, num in enumerate(numbers[:-1]):
            last_spoken[num] = index

        last_num = numbers[-1]
        for index in range(len(numbers) - 1, upperbound - 1):
            num = index - last_spoken[last_num] if last_num in last_spoken else 0
            last_spoken[last_num] = index
            last_num = num

        return last_num
