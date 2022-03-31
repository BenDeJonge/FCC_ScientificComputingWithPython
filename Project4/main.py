# -*- coding: utf-8 -*-
"""
Created on Sun Mar 20 00:53:09 2022

@author: dejong71
"""

#______________________________________________________________________________

import Project4.shape_calculator as shape_calculator
from unittest import main
import os

#______________________________________________________________________________

# Change to Project folder and run unit tests automatically.
rect = shape_calculator.Rectangle(5, 10)
print(rect.get_area())
rect.set_width(3)
print(rect.get_perimeter())
print(rect)

sq = shape_calculator.Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)

os.chdir(os.path.split(__file__)[0])
main(module='test_module', exit=False)

#______________________________________________________________________________