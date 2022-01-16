import sys
sys.path.append('.')

from lib.lect01_uncertainty.uncertainty import (
    Measurement, Decimal
)

from lib.utility.ttype import (
    logging
)

def client_code()->None:
    # mu1 = Measurement(Decimal('5.0'), Decimal('.2'))
    # mu2 = Measurement(Decimal('3.0'), Decimal('.1'))
    # logging.info(f'mu1 = {mu1}; mu2 = {mu2}')
    # logging.info('mu1 + mu2 = {0!r}'.format(mu1 + mu2))
    # logging.info('mu1 < mu2 : {0}\n'.format(mu1 < mu2))

    # mu1 = Measurement(Decimal('10.0'), Decimal('.4'))
    # mu2 = Measurement(Decimal('3.0'), Decimal('.2'))
    # logging.info(f'mu1 = {mu1}; mu2 = {mu2}')
    # logging.info('mu1 - mu2 = {0!r}'.format(mu1 - mu2))
    # logging.info('mu1 == mu2 : {0}\n'.format(mu1 == mu2))

    # mu1 = Measurement(Decimal('6.0'), Decimal('.2'))
    # mu2 = Measurement(Decimal('4.0'), Decimal('.3'))
    # logging.info(f'mu1 = {mu1}; mu2 = {mu2}')
    # logging.info('mu1 * mu2 = {0!r}\n'.format(mu1 * mu2))

    # mu1 = Measurement(Decimal('10.0'), Decimal('.6'))
    # mu2 = Measurement(Decimal('5.0'), Decimal('.2'))
    # logging.info(f'mu1 = {mu1}; mu2 = {mu2}')
    # logging.info('mu1 / mu2 = {0!r}\n'.format(mu1 * mu2))

    # mu1 = Measurement(Decimal('2.0'), Decimal('1.0'))
    # logging.info(f'mu1 = {mu1}')
    # logging.info('mu1.pow(3) = {0!r}\n'.format(mu1.pow(3)))

    # data = [.43, .52, .35, .29, .49]
    # logging.info('calc uncertainty of multi-measurements: {0}\n'.format(Measurement.calc_uncertainty_of_multimeasurements(data)))

    # logging.info('to_absolute: {0}\n'.format(Measurement.to_absolute(Decimal('0.781'), Decimal('0.002560819462227913'))))

    logging.info("\n MIT lect 01, 32:58, t1/t2 = ... ± 0.008, but why? ")
    t1 = Measurement(Decimal('0.781'), Decimal('0.002'))
    t2 = Measurement(Decimal('0.551'), Decimal('0.002'))
    logging.info(t1 / t2)

    mu1 = Measurement(Decimal('148.5'), Decimal('0.5'))
    mu2 = Measurement(Decimal('5.8'), Decimal('0.1'))
    logging.info(repr(mu1 / mu2))

if __name__ == '__main__':
    client_code()
