# coding: utf8

import functools
import operator

from aoc import aoc

# The shifting of coordinates on the grid is pretty simple.
# The overflow (where the grid repeats to the right infinitely) uses otherwise simple math.
# Thank goodness for Python slices.


class Problem(aoc.Problem):
    def solve(self, part):
        rows = self.dataset_lines
        total_trees = []

        pos = 0
        pos_max = len(rows[0])

        if part == 1:
            slopes = [(3, 1)]
        elif part == 2:
            slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

        for shift_right, shift_down in slopes:
            trees = 0
            for row in rows[shift_down::shift_down]:
                pos += shift_right

                # overflow
                while True:
                    pos -= pos_max
                    if pos < 0:
                        # underflow
                        pos += pos_max
                        break

                # This is the tree/square detection.
                if row[pos] == "#":
                    trees += 1

            # reset pos after every slope
            pos = 0
            total_trees.append(trees)

        return functools.reduce(operator.mul, total_trees)
