
class Momentum:
    def __init__(self) -> None:
        pass

    def momentum(self, m:float, v:float)->float:
        '''
        P = m * v;

        unit: kg * m / sec;

        F = ma = m dv/dt = d(mv)/dt = dp/dt;

        it means: a particle changes its momentum, a force must acked upon it;

        vice-verse;

        '''
        return m * v

    def m1_bound_m2_with_spring(self)->str:
        return 'v1 / v2 = m2 / m1'

    def motion_of_center_of_mass(self)->str:
        return 'always perform a const momentum'
