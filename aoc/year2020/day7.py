# coding: utf8

from aoc import aoc

# Day 7 is decidedly more complex than the previous days.
# It involves A LOT of recursion.


class Problem(aoc.Problem):
    def solve(self, part):
        # map of bag colour to other bag colours that can be held
        all_bags = {}
        counter = 0

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

        # bags that can _directly_ contain shiny gold bags go here.
        # Sets are particularly useful because checks are O(1).
        # can_has_shiny_gold = set(k for k, v in all_bags.items() if "shiny gold" in v)

        # Now, we employ some recursion to do the trick.
        def has_shiny_gold(bag):
            nonlocal all_bags
            # nonlocal can_has_shiny_gold
            nonlocal counter

            for inner_bag in all_bags[bag]:

                if inner_bag == "shiny gold":
                    return True
                else:
                    # and so on...
                    return has_shiny_gold(inner_bag)

        return [has_shiny_gold(b) for b in all_bags].count(True)
