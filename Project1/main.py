# -*- coding: utf-8 -*-
"""
Created on Sun Mar 20 00:46:20 2022

@author: dejong71
"""

#______________________________________________________________________________

from arithmetic_arranger import arithmetic_arranger
from pytest import main
import os

#______________________________________________________________________________

# Change to Project folder and run unit tests automatically.
print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))
os.chdir(os.path.split(__file__)[0])
main()

#______________________________________________________________________________