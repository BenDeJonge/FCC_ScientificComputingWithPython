# -*- coding: utf-8 -*-
"""
Created on Sat Mar 19 23:52:29 2022

@author: dejong71
"""

#______________________________________________________________________________

import unittest as ut
from Project1.arithmetic_arranger import arithmetic_arranger

#______________________________________________________________________________

params = [
          [['3801 - 2', '123 + 49']],
          [['1 + 2', '1 - 9380']],
          [['3 + 855', '3801 - 2', '45 + 43', '123 + 49']],
          [['11 + 4', '3801 - 2999', '1 + 2', '123 + 49', '1 - 9380']],
          [['44 + 815', '909 - 2', '45 + 43', '123 + 49', '888 + 40', '653 + 87']],
          [['3 / 855', '3801 - 2', '45 + 43', '123 + 49']],
          [['24 + 85215', '3801 - 2', '45 + 43', '123 + 49']],
          [['98 + 3g5', '3801 - 2', '45 + 43', '123 + 49']],
          [['3 + 855', '988 + 40'], True],
          [['32 - 698', '1 - 3801', '45 + 43', '123 + 49', '988 + 40'], True],
        ]

outputs= [
    '  3801      123\n'
    '-    2    +  49\n'
    '------    -----',

    '  1         1\n'
    '+ 2    - 9380\n'
    '---    ------',

    '    3      3801      45      123\n'
    '+ 855    -    2    + 43    +  49\n'
    '-----    ------    ----    -----',

    '  11      3801      1      123         1\n'
    '+  4    - 2999    + 2    +  49    - 9380\n'
    '----    ------    ---    -----    ------',

    'Error: Too many problems.',

    "Error: Operator must be '+' or '-'.",

    'Error: Numbers cannot be more than four digits.',

    'Error: Numbers must only contain digits.',

    '    3      988\n'
    '+ 855    +  40\n'
    '-----    -----\n'
    '  858     1028',

    '   32         1      45      123      988\n'
    '- 698    - 3801    + 43    +  49    +  40\n'
    '-----    ------    ----    -----    -----\n'
    ' -666     -3800      88      172     1028',
        ]

msgs= [
        'test_two_problems_arrangement1',
        'test_two_problems_arrangement2',
        'test_four_problems_arrangement',
        'test_five_problems_arrangement',
        'test_too_many_problems',
        'test_incorrect_operator',
        'test_too_many_digits',
        'test_only_digits',
        'test_two_problems_with_solutions',
        'test_five_problems_with_solutions',
        ]

#______________________________________________________________________________

for (param, output, msg) in zip(params, outputs, msgs):
    ut.TestCase().assertEqual(arithmetic_arranger(*param),
                              output,
                              msg)

#______________________________________________________________________________