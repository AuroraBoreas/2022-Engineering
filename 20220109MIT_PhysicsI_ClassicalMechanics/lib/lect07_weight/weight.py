
class Weight:
    G:float = +9.8 # unit: m / sec**2

    def __init__(self, mass:float) -> None:
        self._mass = mass

    def weight(self, a:float)->float:
        '''
        using scale to meaure body weight in an elevator
        '''
        return self._mass * (a + self.G)

class WeightOnString:
    G:float = +9.8

    def __init__(self, m1:float, m2:float) -> None:
        self._m1 = m1
        self._m2 = m2

    def av(self)->float:
        '''
        calculate acceleration;
        '''
        return ((self._m2 - self._m1) / (self._m2 + self._m1)) * self.G

    @property
    def string_tension(self)->float:
        '''
        calculate in between tesion;
        '''
        return (2 * self._m1 * self._m2 * self.G) / (self._m1 + self._m2)

def client_code()->None:
    w = Weight(10)
    print(w.weight(10))

    wos = WeightOnString(1.1, 1.25)
    print(wos.av(), wos.string_tension)

if __name__ == '__main__':
    client_code()
