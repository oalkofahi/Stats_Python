import numpy as np
def ECDF(data):
    '''
    Takes a data array (could be a data series)
    Returns x and y for an Empirical Cummulative Distribution Function
    '''
    n = len(data)

    x = np.sort(data)

    y = np.arange(1, n+1)/n

    return x , y