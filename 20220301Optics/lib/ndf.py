"""
Understanding Neutral Density Filters

Neutral Density (ND) filters are designed to reduce transmission evenly across a portion of a specific spectrum. 
ND filters are typically defined by their Optical Density (OD) 
which describes the amount of energy blocked by the filter. 

A high optical density value indicates very low transmission, and 
low optical density indicates high transmission (Equations 1 – 2). 

ND filters can be stacked to achieve a custom optical density. 

To calculate the final system OD, simply add the OD of each filter together.

# terminology
OD : optical density
T  : transmission

# property
T is linear
OD is stackable

# formula
T(Percent Transmission) = 10 ^ -OD * 100%     (1)
OD = -log(T/100%)       (2)

# ref:
https://www.edmundoptics.com/knowledge-center/application-notes/optics/understanding-neutral-density-filters/

# author:
@ZL, 20220301

"""
import math

def transmission(od:float)->float:
    assert od >= 0
    return 10 ** (-1 * od)

def optical_density(t:float)->float:
    assert 0 < t <= 1
    return -1 * math.log10(t)

if __name__ == '__main__':
    od = 0.3 + 1.5
    print(transmission(od))

    t = 0.05
    print(optical_density(t))