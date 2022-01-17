"""
this module is modeling all formulas of MSA part 1: General Measurement System

it has the following functionalities.
- intro: purpose and terminoloy

Author
- @ZL, 20220113

Changelog
- v0.01, initial build

"""

import statistics

class RMS:
    def __init__(self) -> None:
        pass

    @staticmethod
    def bias(x:float, reference_value:float)->float:
        return x - reference_value

    @staticmethod
    def bias_avg(*args)->float:
        return statistics.mean(args)

    @staticmethod
    def sigma_repeatability(*args)->float:
        return statistics.stdev(args)