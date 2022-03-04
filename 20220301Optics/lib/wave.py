from dataclasses import dataclass

from numpy import math

@dataclass
class Wave:
    def __init__(self, wavelength:float=0, frequency:int=0, amplitude:float=0)->None:
        self._wavelength = wavelength 
        self._frequency  = frequency
        self._amplitude  = amplitude

    @property
    def wavelength(self)->float:
        return self._wavelength

    @wavelength.setter
    def wavelength(self, val:float)->None:
        self._wavelength = val

    @property
    def frequency(self)->int:
        return self._frequency

    @frequency.setter
    def frequency(self, val:int)->None:
        self._frequency = val

    @property
    def amplitude(self)->float:
        return self._amplitude

    @amplitude.setter
    def amplitude(self, val:float)->None:
        self._amplitude = val
    
    def speed(self)->float:
        return self._frequency * self._wavelength

    def period(self)->float:
        return 1 / self._frequency

    def __str__(self) -> str:
        return f'\nWavelength: {self._wavelength}\nFrequency: {self._frequency}'

@dataclass
class Colour(Wave):
    light_spead       : float = 2.9e8  # light speed in vaccume
    # spectrum
    red_wavelength    : float = 700    # nm
    red_frequency     : float = 4.3e14 # Hz
    orange_wavelength : float = 600    # nm
    orange_frequency  : float = 5.0e14 # Hz
    yellow_wavelength : float = 580    # nm
    yellow_frequency  : float = 5.2e14 # Hz
    green_wavelength  : float = 550    # nm
    green_frequency   : float = 5.7e14 # Hz
    blue_wavelength   : float = 450    # nm
    blue_frequency    : float = 6.4e14 # Hz
    violet_wavelength : float = 400    # nm
    violet_frequency  : float = 7.5e14 # Hz

    def speed(self) -> float:
        return self.light_spead

    # refraction
    def index_of_refraction(self, velocity_in_vaccum:float, velocity_in_medium:float)->float:
        '''
        
        index of refraction n = (wavelength in vacuum) / (wavelength in medium)

        or return velocity_in_vaccum / velocity_in_medium
        
        because s = vt

        isotropic : uniform index in all directions.

        '''
        return velocity_in_vaccum / velocity_in_medium

    index_of_refraction_ordinary_air : float = 1.000277

    def index_of_refraction_15deg_air(self, wavelength:int)->float:
        '''
        unit of wavelength: um
        '''
        v = 1 / wavelength
        return (8_342.1 + 2_406_030 / (130 - v**2) + 15_996 / (38.9-v**2)) * 1e-8 + 1

    def index_of_refraction_ndeg_air(self, wavelength:int, t:float)->float:
        '''
        pressure is 2e5 / psi

        unit of wavelength: um 
        
        t is temperature: deg
        '''
        return 1 + 1.0549 * self.index_of_refraction_15deg_air(wavelength - 1) / (1 + 0.00366 * t)

    def refraction_angle(self, n1:float, n2:float, I1:float,)->float:
        '''
        
        snell's law

                   \ |
                    \|
            ____________________
                     |\
                     | \
        
        n1 : index of refraction of medium 1

        n2 : index of refraction of medium 2
        
        I1 : incident angle(degree)

        thus, the I2(refraction angle) ∝ λ (wavelength)

        '''
        return n1 * math.sin(I1) / n2
    
    def refraction_distance(self, n1:float, n2:float, d1:float)->float:
        '''
        n1 : index of refraction of medium 1

        n2 : index of refraction of medium 2

        d1 : photon movement in medium 1

        d2 : photon movement in medium 2
        '''
        return n1 * d1 / n2

    def reflection_angle(self, I1:float)->float:
        '''
        I1  : incident angle, unit is degree

        -I1 : reflection angle, unit is degree

        I_incident = - I_reflected
        '''
        return I1

    def bright_nth_newton_ring(self, n:int, R:float, wavelength:float)->float:
        '''
        t: thickness of the air film, unit is meter
        
        r: radius of the ring, unit is meter
        
        D: diameter of the ring, unit is meter

        R: radius of curvature of the lens, unit is meter

        m : mth dark ring, integer
        
        n : nth dark ring, integer

        λ = (Dn^2 - Dm^2) / 4R(n-m), unit must be converted to meter; 1 nm = 1e-9 m;

        t = r**2 / 2 * R   (1)
        
        t = (2n-1) * λ / 4 (2)

        ref: https://scientificsentence.net/Equations/optics/index.php?key=yes&Integer=Newton_rings
        '''
        return math.sqrt(R * (n-1/2) * wavelength)

    def dark_nth_newton_ring(self, n:int, R:float, wavelength:float)->float:
        '''
        ref: https://scientificsentence.net/Equations/optics/index.php?key=yes&Integer=Newton_rings
        '''
        return math.sqrt(R * n * wavelength)

    def const_frequency_of_electromagnetic_radiation(self, wavelength:float)->float:
        '''
        The constant frequency of electromagnetic radiation is given by c/λ
        '''
        return self.light_spead / wavelength

if __name__ == '__main__':
    w = Wave()
    print(w, w.speed())

    c = Colour()
    print(c.speed())

    incident_light_ray_wavelength = 500 # nm
    spherical_lens_radius = 2.00 # m
    # get the radius of 4th bright ring
    r = c.bright_nth_newton_ring(4, spherical_lens_radius, incident_light_ray_wavelength * 1e-9)
    print(r)
