# coding: utf8

import re

from aoc import aoc

# In Python, day 4 is very easy. Dictionaries make field checks trival.
# cid is not required, so it's not here.

# Pre-optimised variables for speed.
REQUIRED = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
RE_HCL = re.compile(r"\#[0-9a-f]{6}")
RE_PID = re.compile(r"^[0-9]{9}$")
EYE_COLOURS = set("amb blu brn gry grn hzl oth".split())


# In part 2, vaildiation is required for each field.
def vaildify(field, value):
    if field == "byr":
        return len(value) == 4 and 1920 <= int(value) <= 2002
    elif field == "iyr":
        return len(value) == 4 and 2010 <= int(value) <= 2020
    elif field == "eyr":
        return len(value) == 4 and 2020 <= int(value) <= 2030
    elif field == "hgt":
        if value.endswith("cm"):
            return 150 <= int(value[:-2]) <= 193
        elif value.endswith("in"):
            return 59 <= int(value[:-2]) <= 76
        else:
            return False
    elif field == "hcl":
        return RE_HCL.match(value) is not None
    elif field == "ecl":
        return value in EYE_COLOURS
    elif field == "pid":
        return RE_PID.match(value) is not None
    elif field == "cid":
        return True


class Problem(aoc.Problem):
    def solve(self, part):
        vaild_passports = 0
        for passport in self.dataset.split("\n\n"):
            passport_map = {
                k: v for k, _, v in (p.partition(":") for p in passport.split())
            }

            if not all(field in passport_map for field in REQUIRED):
                continue

            if part == 2:
                if not all(vaildify(k, v) for k, v in passport_map.items()):
                    continue

            vaild_passports += 1

        return vaild_passports
