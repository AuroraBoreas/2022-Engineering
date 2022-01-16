
import math

class Friction:
    G:float  = +9.8 #unit: m/sec**2
    μs:float = None # const, friction coefficiency to break object static; us > uk;
    μk:float = None # const, friction coefficiency to keep object kinematic

    def __init__(self, mass:float) -> None:
        self._mass = mass

    def force(self, μ:float)->float:
        return μ * self._mass * self.G

    def mu(self, theta:float)->float:
        '''
        put an object on an incline with angle theta;

        increase theta till the object comes to slide;

        μ is independent to mass, contact surface area;

        this is quite non-intuitive;
        '''
        return math.tan(theta)

def client_code()->None:
    pass

if __name__ == '__main__':
    client_code()
