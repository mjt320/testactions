# -*- coding: utf-8 -*-
"""
Created on Sun Sep 26 20:05:51 2021

@author: mjt32
"""
from datetime import datetime

import numpy as np
from src.module import function1

from test.helpers import log_results

def test_function1():
    res = function1()
    np.testing.assert_equal(2,res)
    log_results('Updating results file: ' + str(datetime.now()) + ' ' + str(res) + '\n')
