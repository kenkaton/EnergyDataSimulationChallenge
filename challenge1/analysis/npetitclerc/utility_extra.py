#!/usr/bin/python
"""
Utility functions, not part of sklearn

"""
import numpy as np
from sklearn import utils

def mape(y_true, y_pred): 
    """
    Function to calculate Mean absolute percentage error(MAPE)
    Use of this metric is not recommended; for illustration only. 
    See other regression metrics on sklearn docs:
      http://scikit-learn.org/stable/modules/classes.html#regression-metrics
 
    Use like any other metric
    >>> y_true = [3, -0.5, 2, 7]; y_pred = [2.5, -0.3, 2, 8]
    >>> mape(y_true, y_pred)
    Out[]: 24.791666666666668
    """
    
    y_true, y_pred = utils.check_arrays(y_true, y_pred)
 
    ## Note: does not handle mix 1d representation
    #if _is_1d(y_true): 
    #    y_true, y_pred = _check_1d_array(y_true, y_pred)
 
    return np.mean(np.abs((y_true - y_pred) / y_true)) * 100
