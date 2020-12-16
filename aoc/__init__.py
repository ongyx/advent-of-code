# coding: utf8
"""This module holds all the solutions of the Advent Of Code,
including the datasets for each problem.
"""

import sys

if sys.version_info < (3, 6):
    raise RuntimeError(
        "your python version must be 3.6 or newer (version: %s)"
        % ".".join(map(str, sys.version_info[:3]))
    )

del sys
