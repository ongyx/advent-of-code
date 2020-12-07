# coding: utf8

import re

from aoc import aoc

# We use a regex to parse each line, in the format:
# (min)-(max) (letter): (password)
# For part 2, we need to fidde with the Boolean logic abit.
RE_POLICY = re.compile(r"(\d+)-(\d+) (\w): (\w+)")


class Problem(aoc.Problem):
    def solve(self, part):
        vaild_counter = 0

        for line in self.dataset_lines:
            lower, upper, letter, password = RE_POLICY.findall(line)[0]
            lower = int(lower)
            upper = int(upper)
            if part == 1:
                if lower <= password.count(letter) <= upper:
                    vaild_counter += 1
            elif part == 2:
                # only one of the positions can have the letter
                # so we have to use a XOR (exclusive OR).
                if (password[lower - 1] == letter) ^ (password[upper - 1] == letter):
                    vaild_counter += 1

        return vaild_counter