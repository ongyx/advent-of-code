# coding: utf8

import math

from aoc import aoc

# We can just sort the numbers first, I guess.
# Part 2 requires the Tribonacci sequence.


def tribonacci(num):
    start = [0, 0, 1]
    if num < 2:
        return 1
    elif num == 2:
        return 2

    for index in range(3, num + 3):
        start.append(sum(start[index - n] for n in range(3, 0, -1)))

    return start[-1]


class Problem(aoc.Problem):
    def solve(self, part):
        one_jolts = 0
        three_jolts = 0
        adapters = [0]
        adapters.extend(sorted(self.dataset_numbers, key=int))
        adapters.append(adapters[-1] + 3)
        differences = []
        for index in range(len(adapters)):
            adapter = adapters[index]
            try:
                next_adapter = adapters[index + 1]
            except IndexError:
                # no more to test
                break

            difference = next_adapter - adapter
            differences.append(difference)
            if difference == 1:
                one_jolts += 1
            elif difference == 3:
                three_jolts += 1

        if part == 1:
            return one_jolts * three_jolts
        else:
            permutations = 1
            counter = 0
            for diff in differences:
                if diff == 1:
                    counter += 1
                else:
                    permutations *= tribonacci(counter)
                    counter = 0
            return permutations