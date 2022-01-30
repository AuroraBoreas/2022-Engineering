

import math

class Orbit:
    G:float = 6.67e-11
    T:int   = 24 * 60 * 60  # sec
    R:int   = 6_378 * 1_000 # meter
    M:float = 5.9722e24     # kg

    def __init__(self, r:float) -> None:
        self._r = r

    @property
    def escape_velocity(self)->float:
        '''ME = KE - u

        ME = 1/2 m * v^2 - m * M * G / R

        E >= 0: unbound energy

        E < 0 : bound energy

        '''
        return math.sqrt(2 * self.M * self.G / self.R)

    @property
    def velocity(self)->float:
        '''orbit velocity

        Vorb = (M*G/r) ** 0.5
        '''
        return math.sqrt(self.M * self.G / self._r)

    def period(self)->float:
        return 2 * math.pi * self._r / self.velocity

    def energy(self)->str:
        '''orbit energy
        '''
        return 'ME = 1/2 u = -KE'

class Power:
    heat:float = 1e7 # joule per day

    def __init__(self) -> None:
        pass

    def power(self, f:float, v:float)->float:
        '''Power

        Power = dw/dt

        unit: J/sec = Watt

        dw = F * dr

        P = F * dr / dt = F * v;
        '''
        return f * v

    def calorie(self, joule:float)->float:
        '''chemical energy is same with mechanical energy in essence;
        '''
        return 4.184 * joule

    def Cal(self, calorie:float)->float:
        '''
        1 Cal = 1k calorie
        '''
        return calorie / 1000



def client_code()->None:
    o = Orbit()
    print(o.escape_velocity())

if __name__ == '__main__':
    client_code()
