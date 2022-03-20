# -*- coding: utf-8 -*-
"""
Created on Sun Mar 20 00:50:46 2022

@author: dejong71
"""

#______________________________________________________________________________

from Project2.time_calculator import add_time
from unittest import main
import os

#______________________________________________________________________________

# Change to Project folder and run unit tests automatically.
print(add_time("11:06 PM", "2:02"))
os.chdir(os.path.split(__file__)[0])
main(module='test_module', exit=False)

#______________________________________________________________________________