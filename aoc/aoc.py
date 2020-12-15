# coding: utf8
"""Abstracts an AOC problem."""

import abc
import argparse
import importlib
import pathlib
import sys
import timeit

DATASET_PATH = pathlib.Path(__file__).parent / "datasets"
YEARS = ", ".join([i.name[:4] for i in DATASET_PATH.glob("*") if i.is_dir()])


class Problem(abc.ABC):
    """An AOC problem.

    Args:
        year (int): The year.
        day (int): The day (1-25 inclusive).

    Attributes:
        dataset_path (pathlib.Path): Path to the dataset.
        dataset (str): The dataset.
        dataset_lines (list): The dataset, split as lines.
        dataset_numbers (list): The dataset, split as lines and then casted to ints.
    """

    def __init__(self, year, day) -> None:
        self.dataset_path = DATASET_PATH / str(year) / f"{str(day)}.txt"
        with self.dataset_path.open() as f:
            self.dataset = f.read()

    @abc.abstractmethod
    def solve(self, part):
        """Solve this AOC problem.

        Args:
            part: Which part to solve. Must be 1 or 2.

        Returns:
            The solution.
        """

    @property
    def dataset_lines(self):
        return self.dataset.splitlines()

    @property
    def dataset_numbers(self):
        return [int(i) for i in self.dataset_lines if i.isdigit()]


def main(args=sys.argv[1:]):

    parser = argparse.ArgumentParser(description="""Advent Of Code solver.""")
    parser.add_argument(
        "year", action="store", help=f"AOC year (available: {YEARS})", type=int
    )
    parser.add_argument("day", action="store", help="day to solve for (1-25)", type=int)
    parser.add_argument(
        "-p",
        "--part",
        action="store",
        help="which part to solve for",
        type=int,
        choices=[1, 2],
        default=1,
    )
    options = parser.parse_args(args)

    problem = importlib.import_module(
        f"aoc.year{options.year}.day{options.day}"
    ).Problem(options.year, options.day)
    time_taken = timeit.timeit(
        lambda: print(f"Solution: {problem.solve(options.part)}"), number=1
    )
    print(f"Time taken: {time_taken} seconds")
