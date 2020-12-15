# coding: utf8

from aoc import aoc

EMPTY = "L"
OCCUPIED = "#"
FLOOR = "."


# Because the map cannot change state while checking the seats,
# we keep a 'transaction' of seats to change.


def offsets():
    for r in range(-1, 2):
        for c in range(-1, 2):
            if (r, c) != (0, 0):
                yield r, c


class Problem(aoc.Problem):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.seats = [list(row) for row in self.dataset_lines]

    def commit(self, transaction):
        for status, row, col in transaction:
            self.seats[row][col] = status

    def adjacent_to(self, row, col):
        adj = 0
        for r, c in offsets():
            adj_row = row + r
            adj_col = col + c
            if adj_row < 0 or adj_col < 0:
                continue  # out of bounds

            try:
                if self.seats[adj_row][adj_col] == OCCUPIED:
                    adj += 1
            except IndexError:
                pass
        return adj

    def observed_by(self, row, col):
        obs = 0
        for r, c in offsets():
            next_row = row + r
            next_col = col + c
            while True:
                if next_row < 0 or next_col < 0:
                    break

                try:
                    seat = self.seats[next_row][next_col]
                    if seat == OCCUPIED:
                        obs += 1
                        break
                    elif seat == EMPTY:
                        break
                except IndexError:
                    break  # no more seats to observe

                next_row += r
                next_col += c
        return obs

    def solve(self, part):

        while True:
            transaction = []

            for row in range(len(self.seats)):
                for col in range(len(self.seats[row])):
                    seat = self.seats[row][col]
                    if part == 1:
                        occupied = self.adjacent_to(row, col)
                        occupied_limit = 4
                    elif part == 2:
                        occupied = self.observed_by(row, col)
                        occupied_limit = 5

                    if seat == EMPTY and occupied == 0:
                        transaction.append((OCCUPIED, row, col))
                    elif seat == OCCUPIED and occupied >= occupied_limit:
                        transaction.append((EMPTY, row, col))

            if not transaction:  # no more changes
                break

            self.commit(transaction)

        return sum(r.count(OCCUPIED) for r in self.seats)
