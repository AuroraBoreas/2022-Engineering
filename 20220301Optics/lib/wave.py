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

    # const
    planck_const_h : float = 6.626e34  # Js
    boltzmann_Kb   : float = 1.38e23   # JK

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

    @property
    def quantum_equation(self)->str:
        '''
        P32 / 529

        h : planck's const

        υ : the frequency of the radiation
        
        '''
        return 'E = h * υ'

    @property
    def planck_black_body_law(self)->str:
        '''
        P30 / 529

        h  : planck const

        c  : light speed in vacuum

        λ  : wavelength

        Kb : Boltzmann's constant

        T(K) : temperature of the body

        '''
        return 'Lυ = 2*h*υ^3 / (c^2 * [exp(h*υ/(Kb*T)) - 1])'

    @property
    def wien_display_law(self)->str:
        '''
        P32 / 529
        '''
        return 'λmax * T = constant'

    @property
    def kinetic_energy_of_photoelectron(self)->float:
        '''
        p34 / 529

        m(Kg) : mass
        
        υ(Hz) : frequency

        h     : planck const

        φ     : work function of metal and is the energy required to liberate the electron from the metal surface;
        '''
        return '1/2 * m * υ = h * υ - φ'

    def image_formation_position_of_concave_mirror(self, d0:float, focus_path:float)->float:
        '''
        1 / d0 + 1 / d1 = 1 / focus_path
        '''
        return 1 / (1 / focus_path - 1 / d0)

    @property
    def boltzmann_law(self)->str:
        '''
        P36 / 529

        under conditions of thermal equilibrium the relative populations of a series of energy levels will be given by the Boltzmann law;

        which for two energy levels can be written as:
        
        '''
        return 'N1 / N0 = exp[-(E1 - E0) / (Kb * T)]'

    @property
    def momentum_p_of_partical(self)->str:
        '''
        P34 / 529
        
        E : energy

        m : particle mass

        c : speed of light

        === theory ===

        a) the momentum of a particle is : p = (E^2 - m^2 * c^4)^0.5 / c

        for a photon, m = 0, so : p = E / c

        b) the wavelength of a particle, λ = h / p = h * c / (E^2 - m^c * c^4)^0.5

        for a photon, m = 0, so : λ = h * c / E

        c) the velocity of a particle is : v = p * c^2 / E = c * [1 - (m^2 * c^4 / E^2)]^0.5

        for a photon, m = 0, so : v = c
       
        note: for particle such as electron, mass != zero

        '''
        return 'p = (E^2 - m^2 * c^4)^0.5 / c'

    @property
    def deterministic_laws_of_motion(self)->str:
        return 'Newton\'s law'

    @property
    def laws_of_probability(self)->str:
        return ''

    @property
    def first_order_rate_law(self)->str:
        '''
        P38 / 529

        A10 : Einstein coefficient for spontaneous emission
        
        '''
        return '- dN1 / dt = A10 * N1'

    def optical_path(self, n:float, d:float)->float:
        '''
        P72 / 529

        [d] = n * d

        [d] : optical path

        n   : refractive index

        d   : physical thickness of a material
        '''
        return n * d

    def lorentz_lorenz_equation(self)->str:
        '''
        P79 / 529
        
        N is the number of polarisable units in the material

        αe is the electronic polarisability of each (identical) unit

        note: This equation is only applicable to homogeneous isotropic materials that do not contain
              permanent dipoles or dipolar molecules
        '''
        return '(n^2 - 1) / (n^2 + 2) = N * αe / 3ε0'

    def cauchy_equation(self)->str:
        '''
        P84 / 529

        dispersion and colour produced by dispersion

        for many transparent materials, 
        a good representation of the variation of refractive index with wavelength in the visible region is given by
        Cauchy's equation:
        

        note: for lens design, Cauchy's equation is insufficiently precise
        '''
        return 'n = A + B / λ^2 + C / λ^4'

    def sellmeier_equation(self)->str:
        '''
        P85 / 529

        for a more accurate formula,

        which gives the refractive index of glasses in wavelength range [365nm, 2300nm] to high degree of fidelity

        where the wavelength l is in micrometres and B1 B3 and C1 C3

        are the Sellmeier constants appropriate to the glass

        The Sellmeier equation can also be applied to transparent crystals
        '''
        return 'n = (1 + B1 * λ^2 / (λ^2 - C1) + B2 * λ^2 / (λ^2 - C2) + B3 * λ^2 / (λ^2 - C3))^0.5'

    def coeffecient_of_reflection(self, n0:float, ns:float)->float:
        '''
        P111 / 529

        the amount of light reflected from such a surface depends upon the polarisation of the light
        
        coeffecient of reflection r: define such that if a wave of amplitude ε0 falls upon surface then the amplitude of the reflected wave is rε0

        r = (n0 - ns) / (n0 + ns)

        n0 : refractive index of medium A

        ns : refractive index of medium B
        '''
        return (n0 - ns) / (n0 + ns)

    def reflectance(self, n0:float, ns:float)->float:
        '''
        or reflectivity
        '''
        return self.coeffecient_of_reflection(n0, ns) ** 2

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
