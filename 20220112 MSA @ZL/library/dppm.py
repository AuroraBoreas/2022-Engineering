# https://www.ti.com/support-quality/reliability/DPPM-sample-size-calculator.html

from scipy.stats.distributions import chi2

def dppm(fails:int, cl:float, ss:int)->float:
    '''
    fails: Number of failures in your sample size
    cl   : Confidence Level represented as a decimal
    ss   : Sample size
    DPPM : Defective Parts per million
    '''
    r = 1e6 * chi2.ppf(cl, 2 * fails + 2) / (2 * ss)
    print(f'DPPM is {round(r, 0)} or less with {cl*100}% confidence')
    return 1e6 * chi2.ppf(cl, 2 * fails + 2) / (2 * ss)

if __name__ == '__main__':
    fails  = [2, 2]
    conlvs = [.60, .90]
    ss     = 1_000
    for fail, conlv in zip(fails, conlvs):
        dppm(fail, conlv, ss)
