# coding: utf8

from aoc import aoc


class Problem(aoc.Problem):
    def solve(self, part):
        timestamp = int(self.dataset_lines[0])
        bus_ids = [
            (c, int(i))
            for c, i in enumerate(self.dataset_lines[1].split(","))
            if i != "x"
        ]

        if part == 1:
            departures = {}

            for bus_id in bus_ids:
                bus_id = bus_id[1]
                # find the nearest multiple
                if timestamp % bus_id > 0:
                    nearest = bus_id * ((timestamp // bus_id) + 1)
                else:
                    # the bus arrives on the dot
                    # idk the chances of this happening...
                    nearest = timestamp

                departures[nearest] = bus_id

            earliest = min(departures.keys())
            return departures[earliest] * (earliest - timestamp)
        else:
            # On r/adventofcode, some people solved this using
            # Chinese Remainder Theorem. But I feel this solution is much easier,
            # using the LCM of all the previous buses.
            timestamp = 0
            lcm = 1

            for index in range(len(bus_ids) - 1):
                bus_index, bus_id = bus_ids[index + 1]
                lcm *= bus_ids[index][1]
                while (timestamp + bus_index) % bus_id != 0:
                    timestamp += lcm

            return timestamp
