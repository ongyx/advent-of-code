# advent-of-code

[Advent Of Code](https://adventofcode.com/) solutions in pure Python (no deps outside of stdlib).
Annotations are provided as comments.

Note that the solutions here are not authoritative; they are the author's opinon on the most straightforward (pythonic) way to solve these problems.

Input files (from my run) are already saved here.
It is randomized per user, so you can replace the input files with your own.
The file should be saved at `./aoc/datasets/(year)/(day).txt`.

## 2020

### [Day 1](aoc/year2020/day1.py)

Day 1 is par for the course: some simple bruteforce and math using `random.sample` and a `while` loop.

(Part 1) Your puzzle answer was 913824.
(Part 2) Your puzzle answer was 240889536.

### [Day 2](aoc/year2020/day2.py)

Day 2 needs parsing, but regex can do the trick.
The most interesting part is problably Part 2, because only one of the positions can have the letter.
This is where a XOR (eXclusive OR) comes in handy.

(Part 1) Your puzzle answer was 383.
(Part 2) Your puzzle answer was 272.

### [Day 3](aoc/year2020/day3.py)

Day 3 involves slopes down a mountain that repeats to the right infinitely, which calls for an overflow.
Most of the heavy lifting is done using slices.

(Part 1) Your puzzle answer was 247.
(Part 2) Your puzzle answer was 2983070376.

### [Day 4](aoc/year2020/day4.py)

Day 4, like Day 3, needs parsing but we just need to split by whitespace and use a dictionary to map the fields.
The `vaildify` function checks the fields.

(Part 1) Your puzzle answer was 235.
(Part 2) Your puzzle answer was 194.

### [Day 5](aoc/year2020/day5.py)

Day 5 seats can just be interpreted as base-2 numbers, where `BR` -> 1 and `L` -> 0.
Part 2, because your seat is not at the very front or back, finds the missing seat in the range of seat IDs.

(Part 1) Your puzzle answer was 828.
(Part 2) Your puzzle answer was 565.

### [Day 6](aoc/year2020/day6.py)

Day 6 solution is pretty obvious if you've worked with sets before; we discard any duplicate answers.

(Part 1) Your puzzle answer was 6778.
(Part 2) Your puzzle answer was 3406.

### [Day 7](aoc/year2020/day7.py)

Day 7 is so far the trickiest (to me) because it involves recursion PLUS quite complicated parsing of the input data.
I used dictionaries to keep track of relationships between bags, but I think maybe using a ORM database would be possible.

(Part 1) Your puzzle answer was 101.
(Part 2) Your puzzle answer was 108636.

### [Day 8](aoc/year2020/day8.py)

Day 8 reminds me a lot of Intcode from AOC 2019 (I wasn't there, but apparently it was painful).
We implement an assembly-like language interpreter, so it might reappear in the other days. Who knows?

(Part 1) Your puzzle answer was 1548.
(Part 2) Your puzzle answer was 1375.

### [Day 9](aoc/year2020/day9.py)

Day 9 is like Day 1 (Not bragging, but I got the code for Part 1 correct on the first try).
Part 2 involved more looping (also like Day 1).

(Part 1) Your puzzle answer was 57195069.
(Part 2) Your puzzle answer was 7409241.

### [Day 10](aoc/year2020/day10.py)

WIP