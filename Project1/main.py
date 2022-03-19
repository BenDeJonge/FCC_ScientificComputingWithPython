# -*- coding: utf-8 -*-
"""
Created on Sun Mar 20 00:46:20 2022

@author: dejong71
"""

#______________________________________________________________________________

from pytest import main
import os

#______________________________________________________________________________

# Change to Project folder and run unit tests automatically.
os.chdir(os.path.split(__file__)[0])
main()

#______________________________________________________________________________