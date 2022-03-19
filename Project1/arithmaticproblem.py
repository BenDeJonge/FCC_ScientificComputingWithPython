# -*- coding: utf-8 -*-
"""
Created on Sat Mar 19 21:01:42 2022

@author: dejong71
"""

#______________________________________________________________________________

import string

#______________________________________________________________________________


class ArithmaticProblem:
    
    #__________________________________________________________________________
    
    def __init__(self,
                 problem : str,
                 print_problem : bool = False):
        # Instantiating the attributes.
        self.problem = problem
        self.operator = None
        self.quality_check = None
        self.error = ""
        self.solution = None
        self.lines = None
        self.width = None
        self.formatted_problem = None
        # Checking input data type..
        if not isinstance(self.problem, str):
            self.error = "Error: Problem must a be a string."
            return
        # Splitting the string into its components.
        self.operator = self.get_operator()
        self.lines = self.get_problem_lines()
        # A + or - sign and a space is added in front of the problem,
        # increasing the width by 2 characters.
        self.width = self.find_largest_number_width() + 2
        # Performing input quality tests.
        self.quality_check, self.error = self.check_problem()
        try:
            self.solution = eval(self.problem)
        except SyntaxError:
            self.solution = None
            self.error = "Error: Invalid syntax."
            return
        except ZeroDivisionError:
            self.solution = None
            self.error = "Error: Division by zero."
            return
        # Formatting the output problem.
        if self.solution is not None:# and self.quality_check:
            self.formatted_problem = self.format_problem()
            if print_problem:
                self.print_problem()

    #__________________________________________________________________________

    def check_problem(self):
        '''
        Perform three quality checks on the input problem:\n
            - Check if the problem is an addition or subtraction.\n
            - Check if the problem is purely numeric.\n
            - Check if both numbers are four digits or less.
        '''
        if not self._check_valid_addition_or_subtraction():
            return False, "Error: Operator must be '+' or '-'."
        elif not self._check_only_digits():
            return False, "Error: Numbers must only contain digits."
        elif not self._check_four_digits():
            return False, "Error: Numbers cannot be more than four digits."
        else:
            return True, ""
    
    #__________________________________________________________________________

    def _check_valid_addition_or_subtraction(self):
        '''
        Check if the problem is an addition or subtraction.
        '''
        allowed = '+-'
        not_allowed = '*/'
             
        return any(char in self.problem for char in allowed) and not \
               any(char in self.problem for char in not_allowed)    
    #__________________________________________________________________________

    def _check_only_digits(self):
        '''
        Check if the problem contains only digits and +-.
        '''
        return set(self.problem).issubset(string.digits + '+ -')
    
    #__________________________________________________________________________
    
    def _check_four_digits(self):
        '''
        Check if both numbers are at most 4 digits.
        '''
        return self.width - 2 <= 4.
    
    #__________________________________________________________________________

    def get_problem_lines(self):
        '''
        Isolate both values 
        '''
        lines = max( map(self.problem.split, '+-*/'),
                     key = len )
        return [ s.strip() for s in lines ]
    
    #__________________________________________________________________________

    def get_operator(self):
        for op in '*/+-':
            if op in self.problem:
                return op
    
    #__________________________________________________________________________

    def find_largest_number_width(self):
        '''
        Find the character width of the largest number in the problem.
        '''
        return len( max(self.lines, key=len) )
            
    #__________________________________________________________________________

    def format_problem(self):
        '''
        Generate a formatted problem as a tuple of strings.
        '''
        return (
            f'{self.lines[0]:>{self.width}}',
            f'{self.operator} {self.lines[1]:>{self.width-2}}',
            f'{"-" * self.width}',
            f'{self.solution:>{self.width}}'
            )

    #__________________________________________________________________________

    def print_problem(self):
        for line in self.formatted_problem:
            print(line)
            
    #__________________________________________________________________________


    def __repr__(self):
        return f'ArithmaticProblem\n{self.lines[0]} {self.operator} {self.lines[1]} = {self.solution}'
#______________________________________________________________________________