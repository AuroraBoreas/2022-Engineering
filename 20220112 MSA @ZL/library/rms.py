"""
this module is modeling all formulas of MSA part 1: General Measurement System

it has the following functionalities.
- intro: purpose and terminoloy

Author
- @ZL, 20220113

Changelog
- v0.01, initial build

"""

import statistics

class RMS:
    # section B, Variable Measurement System Study Guidelines
    @property
    def guidelines_for_determining_stability(self)->str:
        return 'Conducting the study:' + \
                    '\n1) obtain a sample and establish its reference value(s) relative to a traceable standard;' + \
                        '\n*if one is not available, select a production part that falls in the mid-range of the production measurements and designate it as the master sample for stability analysis;' + \
                    '\n2) on a periodic basis(daily, weekly), measure the master sample 3~5 times;' + \
                    '\n3) Plot the data on an X-bar&R or X-bar&s control chart in time order;' + \
            '\nAnalysis of Results -- Graphical:' + \
                '\n4) establish control limits and evaluate for out-of-control or unstable conditions using standard chart analysis;' + \
            '\nAnalysis of Results -- Numerical;'

    @property
    def guidelines_for_determining_bias(self)->str:
        '''
        method 01: independent sample method

        method 02: control chart method
        '''
        return 'Conducting the study:' + \
                    '\nHo bias = 0; Ha bias != 0;' + \
                    '\n1) obtain a sample and establish its reference value relative to a traceable standard;' + \
                        '\n*if one is not available, select a production part that falls in the mid-range of the production measurements and designate it as the master sample for bias analysis.' + \
                        '\nmeasure the parts n>=10 times in the gate or tool room, and compute the average of the n readings.' + \
                        '\nuse this average as the "reference value";' + \
                    '\n2) have a single appraiser measure the sample n >= 10 times in the normal manner;' + \
            '\nAnalysis of Results - Graphical:' + \
            '\nAnalysis of Results - Numerical:'
    
    @property
    def guidelines_for_determining_linearity(self)->str:
        return 'Conducting the study;' + \
            '\nanalysis the result -- Graphical;' + \
            '\nanalysis the result -- Numerical;'

    @property
    def guidelines_for_determining_RR(self)->str:
        '''three acceptable methods
        '''
        return 'method 01: range method;' + \
            '\nmethod 02: average and range method (including the Control Chart Method);' + \
            '\nmethod 03: ANOVA method;'

    def bias(x:float, reference_value:float)->float:
        return x - reference_value

    @staticmethod
    def bias_avg(*args)->float:
        return statistics.mean(args)

    @staticmethod
    def sigma_repeatability(*args)->float:
        return statistics.stdev(args)