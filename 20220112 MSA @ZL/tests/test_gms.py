import sys
sys.path.append('.')

from library.gms import GMS


def main()->None:
    g = GMS()
    print(g.basic_equipment)
    g.ms_variability_cause_and_effect_diagram()
    g.establish_needs_of_process_control()
    g.relationship_btwn_bias_and_repeatability()


if __name__ == '__main__':
    main()