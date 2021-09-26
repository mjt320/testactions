# -*- coding: utf-8 -*-
"""
Created on Sun Sep 26 20:12:25 2021

@author: mjt32
"""


def log_results(str):

    filename = './test/results/output.csv'
    with open(filename, 'a', newline='') as f:
        f.write(str)