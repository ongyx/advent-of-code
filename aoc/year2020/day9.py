# coding: utf8

from aoc import aoc

# Like Day 1, I guess.


class Problem(aoc.Problem):
    def solve(self, part):
        dataset = self.dataset_numbers
        dataset_length = len(dataset)
        num_to_check = None  # we need this in outer scope for part 2
        for index in range(25, dataset_length):
            preamble = dataset[index - 25 : index]
            num_to_check = dataset[index]
            vaild_pairs = 0
            for prev1 in range(len(preamble)):
                for prev2 in range(prev1, len(preamble)):
                    if preamble[prev1] + preamble[prev2] == num_to_check:
                        vaild_pairs += 1
            # there must be at least one pair for the number to be vaild
            if not vaild_pairs:
                break

        if part == 1:
            return num_to_check

        # iterate over the whole list
        for index1 in range(0, dataset_length):
            for index2 in range(1, dataset_length):
                numbers = dataset[index1:index2]
                if sum(numbers) == num_to_check:
                    return min(numbers) + max(numbers)
