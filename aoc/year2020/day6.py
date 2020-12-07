# coding: utf8

from aoc import aoc

# Day 6 is easy, because it just involves set operations


class Problem(aoc.Problem):
    def solve(self, part):
        total_yes = 0
        for group in self.dataset.split("\n\n"):
            if part == 1:
                total_yes += len(set(group.replace("\n", "")))
            elif part == 2:
                total_yes += len(set.intersection(*[set(q) for q in group.split("\n")]))

        return total_yes