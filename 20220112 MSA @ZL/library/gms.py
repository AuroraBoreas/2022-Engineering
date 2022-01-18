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
    premis:str      = 'a measurement system operating under stable conditions'
    master:str      = 'true value of a characteristic property'
    bias:str        = 'refers to the location of the data relative to master value'
    variance:str    = 'refers to the spread of the data'
    interaction:str = 'noise: interaction btn the measurement system and its environment'
    guideline:str   = 'it is intended primarily for the measurement system used in the industrial world'

    # chapter I, section A, Intro, Purpose and Terminology;
    @property
    def introduction(self)->str:
        return 'analytic study:' + \
            'increases knowledge about the system of cause and effect of the process; leads ultimately to better understanding of processes'

    @property
    def qod(self)->str:
        return 'quality of measurement data;' + \
            '\nhigh QoD: close to master value;' + \
            '\nlow QoD: far away from master value;'

    @property
    def purpose(self)->str:
        return 'msa purose is to present guidelines for assessing the quality of a measurement system;'

    @property
    def terminology(self)->str:
        return 'terminology:' + \
            '\nMeasurement: the assignment of numbers [or values] to material things to represent the relations among them with respect to particular properties;' + \
            '\nGage: any device used to obtain measurement;' + \
            '\nMeasurement System: the collection of ' + \
                '\ninstruments or gages, ' + \
                '\nstandards, ' + \
                '\noperations, ' + \
                '\nmethods, ' + \
                '\nfixtures, ' + \
                '\nsoftware, ' + \
                '\npersonnel, ' + \
                '\nenvironment, ' + \
                '\nand assumptions used to qualify a unit of measure or fix assessment to the feature characteristic being measured; the complete process used to obtain measurement'
    @property
    def terms(self)->str:
        return 'summary of terms: ' + \
            '\nStandard; ' + \
            '\nBasic equipment; ' + \
            '\nLocation variation; ' + \
            '\nWidth variation; ' + \
            '\nSystem variation;'
            
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
        return '1. Accuracy;' + \
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
    def standards_and_traceability(self)->str:
        '''standard pyramid and traceability chain:
        
        standard pyramid: National <- Ref standard <- Working standard <- Production Gage
        
        traceability chain: wavelength standard <- laser interferometer <- CMM <- Fixture Gae
        '''
        return 'the property of a measurement or the value of a standard whereby it can be related to stated references,' + \
            '\nusually national or international standards,' + \
            '\nthrough an unbroken chain of comparisons all having stated uncertainties;'

    @property
    def national_measurement_institutes(self)->str:
        return 'most of the industrialized countries thoughout the world maintain their own NMIs;'
    
    @property
    def calibration_systems(self)->str:
        return 'a set of operations that establish, under specified conditions, ' + \
            '\n the relationship between a measuring device and a traceable standard of known reference value and uncertainty;'

    @property
    def true_value(self)->str:
        return 'the measurement process TARGET is the "true" value of the part;' + \
            '\nthe "true value" can never be known with certainty;' + \
            '\nuncertainty can be minimized by using a "reference value" based on a well-defined operational definition of the characteristic;'
    
    # chapter I, section B, the Measurement Process;
    @property
    def measurement_systems(self)->str:
        return 'in order to effectively manage variation of any process, there needs to be knowledge of:' + \
            '\n- What the process should be done;' + \
            '\n- What can go wrong;' + \
            '\n- What the process is doing;'
    
    @property
    def statistical_properties_of_ms(self)->str:
        return 'certain fundamental properties that define a "good" MS: ' + \
            '\n1) Adequate discrimination and sensitivity;' + \
            '\n2) The measurement system ought to be in statistical control;' + \
            '\n3) For product control, variability of the ms must be small compared to the specification limits;' + \
            '\n4) For process control, the variability of the ms ought to demonstrate effective resolution and be small compared to manufacturing process variation(6-sigma and/or Total Variation from MSA study);'
    
    @property
    def sources_of_variation(self)->str:
        return '1) Identify the potential sources of variation;' + \
            '\n2) Eliminate (whenever possible) or monitor these sources of variations;'

    def ms_variability_cause_and_effect_diagram(self)->None:
        im = Image.open(ce_path)
        im.show()

    @property
    def effects_of_MS_variability(self)->str:
        return 'Because the output of the MS is used in making a decision about the product and process;' + \
            'the cumulative effect of all the sources of variation is often called "MS error" or "error";'

    @property
    def effect_on_decisions(self)->str:
        return 'Control Philosophy and Driving Interest: ' + \
            '\nProduct control Philosophy: Interest -> Is the part in a specific category?' + \
            '\nProcess Control Philosophy: Interest -> Is the process variation stable and acceptable?'

    @property
    def effect_on_product_decisions(self)->str:
        return 'Type I error: TRUE -> FALSE; producer\'s risk or false alarm;' + \
            '\nType II error: FALSE -> TRUE; consumer\'s risk or miss rate;'

    @property
    def effect_on_process_decisions(self)->str:
        return '1) Statistical control;' + \
            '\n2) On target;' + \
            '\n3) Acceptable variability;'

    @property
    def cmm(self)->str:
        return 'coordinate measuring machine'

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
    def process_control_funnel_experiment(self)->str:
        im = Image.open(fe_path)
        im.show()

        return 'Rule 1: Make no adjustment or take no action unless the process is unstable;' + \
            '\nRule 2: Adjust the process in an equal amount and in an opposite direction from where the process was last measured to be;' + \
            '\nRule 3: Reset the process to the target. then adjust the process in an equal amount and in an opposite direction from the target;' + \
            '\nRule 4: Adjust the process to the point of the last measurement;'

    # chapter I, section C, Measurement Strategy and Planning;
    @property
    def measurement_strategy_and_planning(self)->str:
        return 'Planning is key before designing and purchase of measurement or system:' + \
            '\nCommon sense is the guide in any case;'

    @property
    def complexity(self)->str:
        return 'Any MS may require more or less strategic planning and scrutiny depending on a given produce or process situation.' + \
            '\nthe decision as to the appropriate level shall be left to the APQP team assigned to the measurement process and customer.' + \
            '\nthe actual degree of involvement or implementation in many of the activities below should be driven by the particular MS, consideration of the supporting gage control and calibration system, profound process knowledge, and common sense;'

    @property
    def identify_the_purpose_of_the_measurement_process(self)->str:
        return '1) establish the purpose for the measurement and how the measurement will be utilized; '  + \
            '2) a cross-functional team organized early in the development of the measurement process is critical in accomplishing this task;'

    @property
    def measurement_life_cycle(self)->str:
        return 'MLC: the measurement methods may change over time as one learns and improves the process;' + \
            '\nMost of measuring and monitoring could eventually end up at suppliers of incoming material;' + \
            '\n\nthe same measurement on the same characteristic, at the same area of the process, over an extensive period of time is evidence of a lack of learning or stagnent measurement process;'

    @property
    def criteria_for_a_measurement_process_design_selection(self)->str:
        return 'before a measurement system can be purchased, a detail engineering concept of the measurement process is developed;' + \
            '\nusing the purpose developed above, a cross-functional team of individuals will develop a plan and concept for the MS required by the design; here are some guidelines: ' + \
            '\n 1) the team needs to evaluate the design of the subsystem or component and identify important characteristics;' + \
            '\n 2) using FMEA to capture issues similar;' + \
            '\n 3) develop a flow chart showing critical process steps in the manufacturing or assembly of the part or subsystem;' + \
            '\n 4) identify key inputs and outputs to each step in the process to make a measurement plan, a list of measurement types;' 

    # chapter I, section D, Measurement Source Development;
    @property
    def datum_coordination(self)->str:
        return 'ideally, with the current prevalence in the use of Geometric Dimensioning & Tolerancing(GD&T),' + \
            '\ndatums need to cooridnated(i.e., made identical) throughout the manufacturing process and the MS,' + \
            '\nand this needs to be established very early in the APQP process;' + \
            '\ninitial responsibility for this may lie with the "product design engineer, dimentional control etc.,"'

    @property
    def gage_source_selection_process(self)->str:
        return 'develop the quotation package: ' + \
            '\nDetailed engineering concept; ' + \
            '\nPreventive maintainance consideration;' + \
            '\nSpecifications(Design standards, Build Standards);' + \
            '\nEvaluate the quotations;' + \
            '\nQualification at the Supplier;' + \
            '\nShipment, checklist;' + \
            '\nQualification at the customer;' + \
            '\nDocumentation delivery;'

    # chapter I, section E, Measurement Issues;
    @property
    def measurement_issues(self)->str:
        return '3 fundamental issues must be addressed when evaluating a MS:' + \
            '\n1) the MS must demonstrate adequate sensitivity;' + \
            '\n2) the MS must be stable;' + \
            '\n3) the statistical properties(errors) are consistent over the expected range and adequate for the purpose of measurement(product or process control);'
    
    @property
    def types_of_measurement_system_variation(self)->str:
        return 'MS errors can be classified into five categories: ' + \
            '\n1) bias;' + \
            '\n2) repeatability;' + \
            '\n3) reproducibility;' + \
            '\n4) stability;' + \
            '\n5) linearity;'

    @property
    def definitions_and_potential_sources_of_variation(self)->str:
        return 'Operational definition;' + \
                    '\n1) a specific test of a piece of material or an assembly;' + \
                    '\n2) a criteria for judgement;' + \
                    '\n3) decision: yes or no;' + \
            '\nStandard (NRWG);'  + \
            '\nReference standards;' + \
            '\nMeasurement and test equipment(M&TE);' + \
            '\nCalibration standard;' + \
            '\nTransfer standard;' + \
            '\nMaster;' + \
            '\nWorking standard;' + \
            '\nCheck standard;' + \
            '\nReference value;' + \
            '\nTrue value;' + \
            '\nDiscrimination;'
        
    @property
    def measurement_process_variation(self)->str:
        return 'for most measurement processes, the total measurement variation is usually described as a normal distribution;'

    # chapter I, section F, Measurement Uncertainty;
    # refer to uncertainty library;

    # chapter I, section G, Measurement Problem Analysis;
    @property
    def measurement_problem_anaylsis(self)->str:
        return 'an understanding of measurement variation and the contribution that it makes to total variation((T.V.) needs to be a fundamental step in basic problem solving.' + \
            '\nStep 1) Identify the issue;' + \
            '\nStep 2) Identify the team;' + \
            '\nStep 3) Flowchart of measurement system and process; ' + \
            '\nStep 4) Cause and effect diagram; ' + \
            '\nStep 5) Plan-Do-Study-Act(PDSA);' + \
            '\nStep 6) Possible solution and proof of the correction; ' + \
            '\nStep 7) Institutionalize the change;'

    @property
    def pfmea(self)->str:
        return '1. purpose: define the risk associated with potential process failures;' + \
            '\n2. propose corrective action before these failures can occur;' + \
            '\n\nthe outcome of the PFMEA is transferred to the control plan;'
    
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

    @property
    def tampering(self)->str:
        return 'often manufacturing operations use a single part at the beginning of the day to verify that the process is targeted;' + \
            '\nif the part measured is off target, the process is then adjusted;' + \
            '\nlater, in some cases another part is measured and again the process may be adjusted;'
    
    def relationship_btwn_bias_and_repeatability(self)->None:
        im = Image.open(br_path)
        im.show()

    @property
    def pdsa(self)->str:
        return 'Plan-Do-Study-Act'

    @property
    def pdca(self)->str:
        return 'Plan-Do-Control-Act'