# coding: utf8

import re

from aoc import aoc

# We need to have two masks to correctly overwrite bits: an AND and an OR mask.

RE_MEMSET = re.compile(r"mem\[(\d+)\] = (\d+)")
RE_BITMASK = re.compile(r"mask = ([01X]+)")


def bitstring(num, bits):
    return bin(num)[2:].zfill(bits)


class Problem(aoc.Problem):
    def solve(self, part):
        memory = {}
        mask = None
        and_mask = None
        or_mask = None
        for ins in self.dataset_lines:
            if ins.startswith("mask"):
                mask = RE_BITMASK.findall(ins)[0]
                or_mask = int(mask.replace("X", "0"), 2)
                and_mask = int(mask.replace("X", "1"), 2)
            elif ins.startswith("mem"):
                address, value = RE_MEMSET.findall(ins)[0]
                address, value = int(address), int(value)
                if part == 1:
                    masked_value = (int(value) | or_mask) & and_mask
                    memory[address] = masked_value
                else:
                    address_template = ""
                    # find all permutations
                    for address_bit, mask_bit in zip(bitstring(address, 36), mask):
                        # basically we OR the bit
                        if mask_bit == "0":
                            address_template += address_bit
                        elif mask_bit == "1":
                            address_template += mask_bit
                        elif mask_bit == "X":
                            address_template += "{}"

                    # We iterate through 2 to the power of how many floating bits.
                    floating_len = mask.count("X")
                    for floating in range(2 ** floating_len):
                        memory[
                            int(
                                address_template.format(
                                    *bitstring(floating, floating_len)
                                ),
                                2,
                            )
                        ] = value

        return sum(memory.values())
