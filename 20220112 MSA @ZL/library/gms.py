"""
this module is modeling all formulas of MSA part 1: General Measurement System

it has the following functionalities.
- intro: purpose and terminoloy

Author
- @ZL, 20220112

Changelog
- v0.01, initial build

"""

from PIL import Image

purpose:str = 'analytic study'

why:str = '''
in general, an analytic study is one that increases knowledge about the system of causes that affect the process;

analytic studies are among the most important of measurement data
because they lead ultimately to better understanding of processes;
'''

benefit:str = '''
using a data-based procedure is largely determined by
the quality of the measurement data(QoD) used.

if the data quality is low, the benefit of the procedure is likely to be low;
if the QoD is high, the benefit is likely to be high also;
'''

caution:str = '''
to ensure that the benefit derived from using measurement data is great enough
to warrant the cost of obtaining it, attention needs to be focus on the quality of the data;
'''

what:str = '''
the quality of measurement data(QoD) is defined by the statistical properties of
multiple measurements obtained from a measurement system operating under stable conditions.

for instance, suppose that a measurement system, operating under stable conditions,
is used to obtain several measurements of a certain characteristic.

if the measurements are all "close" to the master value for the characteristic, then the QoD is said to be "high";
similarly, if some, or all, of the measurements are "far away" from the master value, then the QoD is said to be "low";
'''

how:str = '''
the statistical properties most commonly used to characterize the QoD are bias and variance of measurement system(MS);

the property called bias refers to the location of the data relative to a reference(master) value,
the property called variance refers to the spread of the data;
'''

ce_path:str = 'library/diagrams/ms_variability_cause_and_effect_diagram.png'
fe_path:str = 'library/diagrams/deming-funnel-experiment.png'
br_path:str = 'library/diagrams/bias_vs_repeatability.png'

class GMS:
    purpose:str     = 'analytic study'
    why:str         = 'increases knowledge about the system of cause and effect of the process; leads ultimately to better understanding of processes'
    premis:str      = 'a measurement system operating under stable conditions'
    master:str      = 'true value of a characteristic property'
    bias:str        = 'refers to the location of the data relative to master value'
    variance:str    = 'refers to the spread of the data'
    QoD:str         = 'quality of measurement data'
    QoD_high:str    = 'close to master value'
    QoD_low:str     = 'far away from master value'
    interaction:str = 'noise: interaction btn the measurement system and its environment'
    guideline:str   = 'it is intended primarily for the measurement system used in the industrial world'

    @property
    def measurement(self)->str:
        return 'the assignment of numbers [or values] to material things to represent the relations among them with respect to particular properties'

    @property
    def gage(self)->str:
        return 'any device used to obtain measurement'

    @property
    def ms(self)->str:
        return 'the collection of instruments or gages, ' + \
            '\nstandards, ' + \
            '\noperations, ' + \
            '\nmethods, ' + \
            '\nfixtures, ' + \
            '\nsoftware, ' + \
            '\npersonnel, ' + \
            '\nenvironment, ' + \
            '\nand assumptions used to qualify a unit of measure or fix assessment to the feature characteristic being measured; the complete process used to obtain measurement'

    @property
    def standard(self)->str:
        '''
        standard should be an operational definition with which will yield the same results
        when applied by the supplier or customer, with the same meaning yesterday, today and tomorrow;
        '''
        return '1. accept basis for comparison;' + \
            '\n2. criteria for acceptance;' + \
            '\n3. known value, within stated limits of uncertainty, accepted as a true value;' + \
            '\n4. reference value;'

    @property
    def basic_equipment(self)->str:
        return '1. discrimination, readability, resolution;' + \
            '\n2. effective resolution;' + \
            '\n3. Reference value;' + \
            '\n4. True value;'

    @property
    def location_variation(self)->str:
        return '1. Accurary;' + \
            '\n2. Bias;' + \
            '\n3. stability(alias drift);' + \
            '\n4. linearity(a systematic error component of MS);'

    @property
    def width_variation(self)->str:
        return '1. Precision;' + \
            '\n2. Repeatability(E.V., within-system variation);' + \
            '\n3. Reproducibility(A.V.,);' + \
            '\n4. GRR or Gage R&R;' + \
            '\n5. Measurement System Capability(short-term ms variation);' + \
            '\n6. Measurement System Performance(long-term control chart method);' + \
            '\n7. Sensitivity;' + \
            '\n8. Consistency;' + \
            '\n9. Uniformity;'

    @property
    def system_variation(self)->str:
        '''
        all characterization of the total variation of the measurement system
        assume that the system is stable and consistent.
        '''
        return '1. Capability;' + \
            '\n2. Performance;' + \
            '\n3. Uncertainty;'
    
    @property
    def nmi(self)->str:
        return 'National Measurement Institute'

    @property
    def traceability(self)->str:
        return 'the property of a measurement or the value of a standard whereby it can be related to stated references,' + \
            '\nusually national or international standards,' + \
            '\nthrough an unbroken chain of comparisons all having stated uncertainties;'

    @property
    def true_value(self)->str:
        return 'the measurement process TARGET is the "true" value of the part;' + \
            '\nthe "true value" can never be known with certainty;' + \
            '\nuncertainty can be minimized by using a "reference value" based on a well-defined operational definition of the characteristic;'

    @property
    def pfmea(self)->str:
        return '1. purpose: define the risk associated with potential process failures;' + \
            '\n2. propose corrective action before these failures can occur;' + \
            '\n\nthe outcome of the PFMEA is transferred to the control plan;'
    
    @property
    def fundamental_properties_of_good_measurement_system(self)->str:
        return '1) Adequate discrimination and sensitivity;' + \
            '\n2) The measurement system ought to be in statistical control;' + \
            '\n3) For product control, variability of the ms must be small compared to the specification limits;' + \
            '\n4) for process control, the variability of the ms ought to demonstrate effective resolution and be small compared to manufacturing process variation(6-sigma and/or Total Variation from MSA study);'

    @property
    def sources_of_variation(self)->str:
        return '1) Identify the potential sources of variation;' + \
            '\n2) Eliminate (whenever possible) or monitor these sources of variations;'
    
    @property
    def present_and_categorize_sources_of_variation(self)->str:
        return '1) cause-effect diagrams;' + \
            '\n2) fault-tree diagrams;' + \
            '\n3) S.W.I.P.E;'

    @property
    def swipe(self)->str:
        return 'S: standard;' + \
            '\nW: workpiece;' + \
            '\nI: instrument;' + \
            '\nP: person/procedure;' + \
            '\nE: environment;'
    
    def ms_variability_cause_and_effect_diagram(self)->None:
        im = Image.open(ce_path)
        im.show()

    @property
    def product_control_philosophy(self)->str:
        return 'Driving interest: is the part in a specific category?'

    @property
    def process_control_philosophy(self)->str:
        return 'Driving interest: is the process variation stable and acceptable?'

    @property
    def cmm(self)->str:
        return 'coordinate measuring machine'

    def establish_needs_of_process_control(self)->str:
        return '1) Statistical control;' + \
            '\n2) On target;' + \
            '\n3) Acceptable variability;'

    @staticmethod
    def variation_obs(variation_act:float, variation_msa:float)->float:
        """the basic relationship btwn the actual and the observed variation is:
        variation_obs = variation_act + variation_msa

        Args:
            variation_act (float): actual process variance
            
            variation_msa (float): variance of measurement system

        Returns:
            float: observed process variance
        """
        return variation_act + variation_msa

    @staticmethod
    def cp_index(tolerance_range:float, sigma:float)->float:
        return tolerance_range / (6 * sigma)

    @staticmethod
    def cp_obs(cp_act:float, cp_msa:float)->float:
        """the relationship btwn the Cp index of the observed process
        and the Cp indices of the actual process
        and the measurement system is derived by substituting the equation for Cp into the observed variance equation above;
        
        (Cp_obs) ** -2 = (Cp_act) ** -2 + (Cp_msa) ** -2

        Args:
            cp_act (float): [description]
            
            cp_msa (float): [description]

        Returns:
            float: [description]
        """
        return cp_act ** (-2) + cp_msa ** (-2)

    @property
    def tampering(self)->str:
        return 'often manufacturing operations use a single part at the beginning of the day to verify that the process is targeted;' + \
            '\nif the part measured is off target, the process is then adjusted;' + \
            '\nlater, in some cases another part is measured and again the process may be adjusted;'
    
    @property
    def four_rules_of_funnel_experiment(self)->str:
        im = Image.open(fe_path)
        im.show()

        return 'Rule 1: Make no adjustment or take no action unless the process is unstable;' + \
            '\nRule 2: Adjust the process in an equal amount and in an opposite direction from where the process was last measured to be;' + \
            '\nRule 3: Reset the process to the target. then adjust the process in an equal amount and in an opposite direction from the target;' + \
            '\nRule 4: Adjust the process to the point of the last measurement;'

    def relationship_btwn_bias_and_repeatability(self)->None:
        im = Image.open(br_path)
        im.show()

    @property
    def pdsa(self)->str:
        return 'Plan-Do-Study-Act'

    @property
    def pdca(self)->str:
        return 'Plan-Do-Control-Act'