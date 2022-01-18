"""
this module is modeling all formulas of MSA part 2: Assessing Measurement System

it has the following functionalities.
- intro: purpose and terminoloy

Author
- @ZL, 20220112

Changelog
- v0.01, initial build

"""

class AMS:
    # section A, Background
    @property
    def background(self)->str:
        return 'two important areas need to be assessed: ' + \
            '1) verify the correct variable is being measured at the proper characteristic location;' + \
            '2) determine what statistical properties the MS needs to have in order to be acceptable;'

    @property
    def phase_01(self)->str:
        return 'testing is an assessment to verify the correct variable is being measured at the proper characteristic location per measurement system design specification;'

    @property
    def phase_02(self)->str:
        return 'testing provides ongoing monitoring of the key sources of variation for continued confidence in the measurement system (and the data being generated);' + \
            '\nand/or a signal that the measurement system has a degraded over time;'

    # section B, selecting/developing test procedures
    @property
    def selecting_or_developing_test_procedure(self)->str:
        return '1. should standards, such as those traceable to NIST, be used in the testing and, if so, what level of standard is appropriate?' + \
            '\n2. for the ongoing testing in Phase 2, the use of blind measurements may be considered.' + \
            '\n3. the cost of testing' + \
            '\n4. the time required for the testing' + \
            '\n5. any term for which there is no commonly accepted definition should be operationally defined (terms: accuracy, precision, repeatability, reproducibility etc.,).' + \
            '\n6. will the measurements made by the MS be compared with measurements made by another system?' + \
            '\n7. how often should Phase 2 testing be performed?'

    # section C, preparation for a MS study
    @property
    def prep_measurement_system_study(self)->str:
        return '1) the approach to be used should be planned;' + \
            '\n2) the number of appraisers, number of sample parts, and number of repeat readings should be determined beforehand:' + \
                '\na) Criticalilty of dimension;' + \
                '\nb) Part configuration;' + \
                '\nc) Customer requirements;' + \
            '\n3) the appraises chosen should be selected from those who normally operate this instrument;' + \
            '\n4) selection of the sample parts is critical for proper analysis and depends entirely upon the design of the MSA study, purpose of the measurement system, and availability of part samples that represent the production process;' + \
            '\n5) the instrument should have a discrimination that allows at least one-tenth of the expected process variation of the characteristic to be read directly;' + \
            '\n6) assure that the measuring method (i.e., appraiser and instrument) is measuring the dimension of the characteristic and is following the defined measurement procedure;'
    
    @property
    def conduct_study_in_manner(self)->str:
        return '1) the measurements should be made in a "random order" to ensure that any drift or changes that could occur will be spread randomly throughout the study;' + \
            '\n2) in reading the equipment, measurement valeus should be recorded to the practical limit of the instrument discrimination;' + \
            '\n3) the study should be managed and observed by a person who unnderstands the importance of conducting a reliable study;'

    @property
    def consider_several_factors_to_develop_phase1_2_test_programs(self)->str:
        return '- what effect does the appraiser have on the measurement process?' + \
            '\n- is appraiser calibration of the measurement equipment likely to be a significant cause of variation?' + \
            '\n- how many sample parts and repeated readings are required?'

    # section D, Analysis of the Results
    @property
    def analysis_of_results(self)->str:
        return 'Assembly or fixture error;' + \
            '\nLocation error;' + \
            '\nWidth error;'

    @property
    def for_product_control_situation(self)->str:
        return 'where the measurement result and decision criteria determine, "conformance or nonconformance to the feature specification"' + \
            '\nsamples(or standards) must be selected, but need not cover the entire process range.' + \
            '\nthe assessment of the measurement system is based on the feature tolerance(i.e., %GRR to TOLERACNE)'

    @property
    def for_process_control_situation(self)->str:
        return 'where the measurement reesult and decision criteria determine, "process stability, direction and compliance with the natural process variation" is recommended when assessing the adequacy(i.e., SPC)' + \
            '\nwhen assessing the adaquacy of the measurement system for process control (i.e., %GRR to prcess variation)'

    @property
    def pv(self)->str:
        return 'the variation in sample parts(PV)'
    
    @property
    def tv(self)->str:
        return 'total variation'

    @staticmethod
    def grr_criteria(grr:float)->str:
        if grr < 0:
            raise ValueError('grr must be in [0, 1]')

        if grr < 0.1:
            return 'generally considered to be an acceptable measurement system'
        elif 0.1 <= grr < 0.3:
            return 'May be acceptable for some applications'
        else:
            return 'Considered to be unacceptable'