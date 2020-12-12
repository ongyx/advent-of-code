# coding: utf8

import copy

from aoc import aoc

EMPTY = "L"
OCCUPIED = "#"
FLOOR = "."


class Problem(aoc.Problem):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.layout = [list(row) for row in self.dataset_lines]

    def solve(self, part):
        did_changed = False
        seats = copy.deepcopy(self.layout)
        while not did_changed:
            # FIXME: not done yet
            break
