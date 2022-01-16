"""

this module is to calculate meansurement uncertainty.

## Why
Walter Lewin @MIT, 2015:
"Any measurement you make w/o the knowledge of its uncertainty is meaningless;

## What
what is measurement uncerntainty?
whenever you make a measurement while collecting data,
you can assume that there is a "true value"
that falls within the range of the measurements you made.

you need to find the best estimate of your measurement and consider the results
when you add or substract the measurement uncertainty.

## How
how to perform airthmetic oprations?
link: https://www.wikihow.com/Calculate-Uncertainty

## Author
@ZL, 20220109

## Changelog
- v0.01, initial build

"""

from __future__ import annotations
from decimal import Decimal
from functools import total_ordering
from typing import List
import statistics

@total_ordering
class Measurement:
    _meas_val:Decimal = None # measurement value, unit is same by default
    _meas_unc:Decimal = None # measurement uncertainty, unit is same by default

    def __init__(self, mv:Decimal, mu:Decimal) -> None:
        """init object with measurement value, measurement uncertainty

        Args:
            mv (Decimal): measurement value

            mu (Decimal): measurement uncertainty

        Raises:
            ValueError: the decimal places of measurement value and uncertainty must match
        """
        if mv.as_tuple().exponent != mv.as_tuple().exponent:
            raise ValueError("measurement value and uncertainty must have same decimal places, for example: 3.14 ± 0.12")
        self._meas_val = mv
        self._meas_unc = mu

    def __str__(self) -> str:
        return f'{self._meas_val} ± {self._meas_unc}'

    def __repr__(self) -> str:
        return f'absolute: ({self.__str__()}); relative: ({self.to_relative()})'

    @property
    def relative_uncertainty(self) -> float:
        return self._meas_unc / self._meas_val

    def to_relative(self) -> str:
        return f'{self._meas_val} ± {self.relative_uncertainty * 100}%'

    @staticmethod
    def to_absolute(mv:Decimal, ru:Decimal) -> str:
        """return absolute measurement uncertainty from a given absolute uncertainty

        Args:
            mv (Decimal): measurement value

            ru (Decimal): relative uncertainty(%)

        Returns:
            str: measurement object
        """
        return Measurement(mv, mv * ru)

    @staticmethod
    def calc_uncertainty_of_multimeasurements(measurements: List[float]) -> Measurement:
        """return measurement object from a give list with measurement results insie

        Args:
            measurements (List[float]): measurement results, like [3.14, 2.718, 1,818, ...]

        Returns:
            Measurement: Measurement object
        """
        means:str = statistics.mean(measurements).__str__()
        sd:str    = statistics.stdev(measurements).__str__()
        return Measurement(Decimal(means), Decimal(sd))

    def __eq__(self, other: Measurement) -> bool:
        return self._meas_val == other._meas_val

    def __le__(self, other: Measurement) -> bool:
        return self._meas_val < other._meas_val

    def __add__(self, other: Measurement) -> Measurement:
        return Measurement(self._meas_val + other._meas_val, self._meas_unc + other._meas_unc)

    def __sub__(self, other: Measurement) -> Measurement:
        return Measurement(self._meas_val - other._meas_val, self._meas_unc + other._meas_unc)

    def __mul__(self, other: Measurement) -> Measurement:
        new_mv = self._meas_val * other._meas_val
        return Measurement(new_mv, new_mv * (self.relative_uncertainty + other.relative_uncertainty))

    def __truediv__(self, other: Measurement) -> Measurement:
        new_mv = self._meas_val / other._meas_val
        return Measurement(new_mv, new_mv * (self.relative_uncertainty + other.relative_uncertainty))

    def pow(self, p:int) -> Measurement:
        # new_mv = math.pow(self._meas_val, p) not work, using dunder method Decimal.__pow__() instead
        new_mv = self._meas_val.__pow__(p)
        new_mu = self.relative_uncertainty * p
        return Measurement(new_mv, new_mv * new_mu)
