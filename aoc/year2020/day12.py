# coding: utf8

from aoc import aoc


class Problem(aoc.Problem):
    def solve(self, part):
        if part == 1:
            pos = [0, 0]
            waypoint = [0, 0]
        else:
            pos = [0, 0]
            waypoint = [10, 1]
        cardinals = ["N", "E", "S", "W"]
        direction = 90
        directions = {n: c for n, c in zip([0, 90, 180, 270], cardinals)}

        def execute(action, value):
            nonlocal part
            nonlocal pos
            nonlocal waypoint
            nonlocal direction
            if action == "N":
                waypoint[1] += value
            elif action == "S":
                waypoint[1] -= value
            elif action == "E":
                waypoint[0] += value
            elif action == "W":
                waypoint[0] -= value
            elif action == "R":
                direction += value
                if direction >= 360:
                    # overflow back to 0
                    direction = direction % 360
            elif action == "L":
                direction -= value
                if direction < 0:
                    # underflow
                    direction = 360 + direction
            elif action == "F":
                curdir_x = directions[direction]
                curdir_y = cardinals[cardinals.index(curdir_x) - 1]
                print(curdir_x, curdir_y)
                if part == 1:
                    execute(curdir_x, value)
                else:
                    # waypoint is relative
                    # we have to consider the direction as relative...
                    forward_x = (
                        -(waypoint[0] * value)
                        if curdir_x in ("S", "W")
                        else waypoint[0] * value
                    )
                    forward_y = (
                        -(waypoint[1] * value)
                        if curdir_y in ("S", "W")
                        else waypoint[1] * value
                    )

                    if curdir_x in ("S", "N") and curdir_y in ("W", "E"):
                        # swap directions
                        forward_x, forward_y = forward_y, forward_x

                    pos[0] += forward_x
                    pos[1] += forward_y

            if part == 1:
                pos = waypoint

        for nav in self.dataset_lines:
            execute(nav[0], int(nav[1:]))
            print(*pos, *waypoint, direction)
        return abs(pos[0]) + abs(pos[1])
