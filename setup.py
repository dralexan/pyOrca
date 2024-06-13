# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 17:29:28 2024

@author: DAlexander, imported from GPT
"""

from setuptools import setup, find_packages

setup(
    name='pyOrca',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'pymodbus', 'struct', 'time'
    ],
    description='A Python package for communicating with the Orca motor using Modbus.',
    author='Daniel Alexander',
    author_email='support@irisdynamics.com',
    url='https://github.com/yourusername/pyOrca',  
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)