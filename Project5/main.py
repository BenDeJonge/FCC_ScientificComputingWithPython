# -*- coding: utf-8 -*-
"""
Created on Sun Mar 20 00:54:15 2022

@author: dejong71
"""

#______________________________________________________________________________

import prob_calculator
from unittest import main
import os

#______________________________________________________________________________

# Change to Project folder and run unit tests automatically.
prob_calculator.random.seed(95)
hat = prob_calculator.Hat(blue=4, red=2, green=6)
probability = prob_calculator.experiment(
    hat=hat,
    expected_balls={"blue": 2,
                    "red": 1},
    num_balls_drawn=4,
    num_experiments=3000)
print("Probability:", probability)

os.chdir(os.path.split(__file__)[0])
main(module='test_module', exit=False)

#______________________________________________________________________________