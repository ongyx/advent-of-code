# coding: utf8

import random

from aoc import aoc

# There are two ways to solve this.
# 1. Bruteforce by using random.sample to get two unique integers from the dataset.
# 2. Iterate over the dataset using nested for loops.
# (2) is problably O(n^3), how long (1) takes is anyone's guess.
# The same two methods can be used for part 2, by sampling 3 ints or having 3 nested for loops.

# But bruteforce seems more fun, right?
class Problem(aoc.Problem):
    def solve(self, part):
        # bruteforce
        if part == 1:
            while True:
                exp1, exp2 = random.sample(self.dataset_numbers, 2)
                if exp1 + exp2 == 2020:
                    return exp1 * exp2
        elif part == 2:
            while True:
                exp1, exp2, exp3 = random.sample(self.dataset_numbers, 3)
                if exp1 + exp2 + exp3 == 2020:
                    return exp1 * exp2 * exp3
