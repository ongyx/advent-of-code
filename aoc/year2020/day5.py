# coding: utf8

from aoc import aoc

# here, we use a range.
# Python slices to the rescue again!
# In part 2, sets are very useful in checking which seat id is missing.


class Problem(aoc.Problem):
    def solve(self, part):
        seat_ids = []
        for seat in self.dataset_lines:
            # lol, it can be interpreted as a base-2 number
            seat_ids.append(int("".join(["1" if c in "BR" else "0" for c in seat]), 2))

        seat_ids.sort(key=int)
        first = seat_ids[0]
        last = seat_ids[-1]

        if part == 1:
            return last
        elif part == 2:
            # find the seat id not present in the list
            seat_ids = set(seat_ids)
            for seat_id in range(first, last + 1):
                if seat_id not in seat_ids:
                    return seat_id
