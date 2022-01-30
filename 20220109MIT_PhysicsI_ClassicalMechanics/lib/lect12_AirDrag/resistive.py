

import math

class Resistive:
    air_c1:float = 3.1e-4
    air_c2:float = 0.85

    def __init__(self) -> None:
        pass

    def force(self)->str:
        return '-1 * (k1 * v + k2 * v**2) * v-hat'

    def sphere(self)->str:
        '''
        Sphere |Fres| = C1 * r * v + C2 * r**2 * v**2

        C1: coeffeciency of viscous; region I is dominates;

        C2: coeffeciency of pressure; region II dominates;

        C2 and ρ are strongley related;
        '''
        return 'C1 * r * v + C2 * r**2 * v**2'

    def sphere_v_crit(self)->str:
        return 'C1 / (C2 * r)'

    def sphere_v_terminal(self)->str:
        return 'C2 * r**2 * v**2 + C1 * r * v - mg = 0'
