# coding: utf8

import sys

from aoc import aoc

# Day 7 is decidedly more complex than the previous days.
# It involves A LOT of recursion.


class Problem(aoc.Problem):
    def solve(self, part):
        # map of bag colour to other bag colours that can be held
        all_bags = {}

        # parse the dataset first
        for bag in self.dataset_lines:
            bags = bag.split()
            bag_colour = " ".join(bags[:2])
            all_bags[bag_colour] = {}
            for index in range(4, len(bags), 4):
                inner_bag_count = bags[index]
                if inner_bag_count == "no":
                    # bag cannot contain any other bag
                    break

                inner_bag_colour = " ".join(bags[index + 1 : index + 3])
                all_bags[bag_colour][inner_bag_colour] = int(inner_bag_count)

        # Now, we employ some recursion to do the trick.
        def has_shiny_gold(bag):
            nonlocal all_bags

            return any(b=="shiny gold" or has_shiny_gold(b) for b in all_bags[bag])

        def count_in_shiny_gold(bag="shiny gold"):
            nonlocal all_bags
            
            return sum(bc + (bc * count_in_shiny_gold(b)) for b, bc in all_bags[bag].items())

        if part == 1:
            return sum(has_shiny_gold(b) for b in all_bags)
        elif part == 2:
            return count_in_shiny_gold()
