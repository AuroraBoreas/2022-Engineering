
class Spring:
    def __init__(self, k:float, x:float) -> None:
        self._k = k
        self._x = x

    def potential_energy(self)->float:
        return 0.5 * self._k * self._x ** 2
