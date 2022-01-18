#

from PIL import Image
pismoea_path:str = 'library\diagrams\pismoea.png'

class OMS:
    @property
    def practices_for_non_replicable_measurement_system(self)->str:
        '''for example:

        destructive MS;

        systems when the part changes on use/test;
        '''
        return 'not all measurement systems where the readings can be replicated for each part;'


    @property
    def single_part_single_measurement_per_cycle(self)->str:
        '''P.164/241
        '''
        return 'Application:' + \
                    'a) MS in which the part is not changed by the measurement process(static properties, or dynamic properties);' + \
                    'b) the shelf life of the characteristic (property) is known and extends beyond the expected duration of the study;' + \
            'Assumptions: ' + \
                '* MS is known (documented) to have a linear response over the expected range of the characteristic(property);' + \
                '* Parts (specimens) cover the expected range of the process variation of the characteristic;' + \
            'Analyze using X & mR charts:' + \
                'Determine MS stability;' + \
                'Compare s = R-bar/d (total measurement error) with the repeatability estimate s from a variability study;' + \
                'Determine the bias if reference value is known;'

    @property
    def parts_n_gt_3_single_measurement_per_cycle_per_part(self)->str:
        '''P.165/241
        '''
        return 'Application:' + \
                    'a) MS in which the part is not changed by the measurement process(static properties, or dynamic properties);' + \
                    'b) the shelf life of the characteristic (property) is known and extends beyond the expected duration of the study;' + \
            'Assumptions: ' + \
                '* MS is known (documented) to have a linear response over the expected range of the characteristic(property);' + \
                '* Parts (specimens) cover the expected range of the process variation of the characteristic;' + \
            'Analyze using a|z, R| chart: where z = x - μ; ...'

    @property
    def large_sample_from_a_stable_process(self)->str:
        '''p.166/241
        '''
        return 'Application - Assumptions - Analyze using'

    def pismoea(self)->None:
        im = Image(pismoea_path)
        im.show()