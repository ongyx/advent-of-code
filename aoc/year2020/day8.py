# coding: utf8

from aoc import aoc

# ngl getting some Intcode vibes here.


# fun fact: The instructions (acc, jmp, nop) are basically a subset of Brainfuck
# (hence the name) but there is only one memory cell:
# acc -> (+/-)
# jmp -> ([/])
# nop -> ()
# It wouldn't be so hard to make a Bootfuck -> Brainfuck compiler.
class Bootfuck:
    def __init__(self, bootcode):
        self.bootcode = []
        self.executed = set()
        self.program_counter = 0
        self.accumulator = 0
        self.status = None

        if not isinstance(bootcode, list):
            bootcode = bootcode.splitlines()

        for inst in bootcode:
            if isinstance(inst, tuple):
                break
            op, _, arg = inst.partition(" ")
            self.bootcode.append((op, int(arg)))

        self.bootcode_length = len(self.bootcode)

    def execute(self):
        while True:
            if self.program_counter in self.executed:
                # HALT!!!1!
                # maybe i should add a HCF instruction...
                self.status = "inf"
                break
            elif self.program_counter == self.bootcode_length - 1:
                self.status = "halt"
                break
            else:
                self.executed.add(self.program_counter)

            op, arg = self.bootcode[self.program_counter]
            if op == "acc":
                self.accumulator += arg
            elif op == "jmp":
                self.program_counter += arg - 1
            elif op == "nop":
                pass

            self.program_counter += 1

        return self.accumulator


class Problem(aoc.Problem):
    def solve(self, part):
        interpreter = Bootfuck(self.dataset_lines)
        if part == 1:
            return interpreter.execute()
        elif part == 2:
            swap = {"nop": "jmp", "jmp": "nop"}
            # yay more bruteforce
            for index, (op, arg) in enumerate(interpreter.bootcode):
                if op in swap:
                    new_interpreter = Bootfuck(self.dataset_lines)
                    new_interpreter.bootcode[index] = (swap[op], arg)
                    result = new_interpreter.execute()
                    if new_interpreter.status == "halt":
                        return result
