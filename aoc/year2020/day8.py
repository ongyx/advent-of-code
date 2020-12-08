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
        self.program_counter = -1
        self.accumulator = 0
    
        if not isinstance(bootcode, list):
            bootcode = bootcode.splitlines()
        
        for inst in bootcode:
            op, _, arg = inst.partition(" ")
            self.bootcode.append((op, int(arg)))
    
    def acc(self, arg):
        self.accumulator += arg
    
    def jmp(self, arg):
        self.program_counter += arg
    
    def nop(self, arg):
        pass
    
    def execute_op(self, op, arg):
        self.__dict__[op](arg)
    
    def execute(self):
        while True:
            self.program_counter += 1
            if self.program_counter in self.executed:
                # HALT!!!1!
                # maybe i should add a HCF instruction...
                break
            else:
                self.executed.add(self.program_counter)
            
            self.execute_op(*self.bootcode[self.program_counter])

        return self.accumulator


class Problem(aoc.Problem):
    def solve(self, part):
        interpreter = Bootfuck(self.dataset_lines)
        return interpreter.execute()