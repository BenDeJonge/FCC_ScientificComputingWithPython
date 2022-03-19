# -*- coding: utf-8 -*-
"""
Created on Sat Mar 19 22:46:13 2022

@author: dejong71
"""

#______________________________________________________________________________

from Project1.arithmaticproblem import ArithmaticProblem

#______________________________________________________________________________

def arithmetic_arranger(problems : list, show_solution=False):
    # Avoiding printing too many problems.
    if len(problems) > 5:
        return 'Error: Too many problems.'
    # Storing problems in memory.
    aps = [ ArithmaticProblem(p) for p in problems ]
    # If no problem returns an error, group the outputs in a large string.
    if all([ ap.quality_check for ap in aps ]):       
        lines = ['' for i in range(4)]
        for ap in aps:
            for i, line in enumerate(ap.formatted_problem):
                lines[i] += line + 4 * ' '
        lines = [line.rstrip() for line in lines ]
        # Printing problem and solution separately.
        for line in lines[:-1]:
            print(line)
        if show_solution:
            print(lines[-1])
        return '\n'.join(lines)
    # If any problem returns an error, display the first error.
    else:
        for ap in aps:
            if ap.error != '':
                if show_solution:
                    print(ap.error)
                return ap.error
            
#______________________________________________________________________________