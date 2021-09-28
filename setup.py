# -*- coding: utf-8 -*-
"""
Created on Tue Sep 28 14:54:45 2021

@author: mjt32
"""

from setuptools import setup, find_packages


setup(
        name='src',
        version = '1.0.0', 
        install_requires = ['numpy'],
        packages = find_packages()
        )