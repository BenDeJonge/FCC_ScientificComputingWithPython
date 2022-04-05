# -*- coding: utf-8 -*-
"""
Created on Sun Apr  3 15:17:38 2022

@author: dejong71
"""

#===IMPORTS====================================================================

import copy
import random
from scipy.stats import multivariate_hypergeom

#==============================================================================

class Hat:
    '''
    A model for a Hat containing colored balls.

    Parameters
    ----------
    **colors : int
        The counts of colored balls inside the hat, e.g. Hat(red=3, blue=2).

    Returns
    -------
    None.
    '''
    
    #---INITIALIZATION---------------------------------------------------------
    
    def __init__(self, **colors):
        self.colors = colors
        self.contents = self.dict_to_list(self.colors)
    
    #---REPRESENTATION---------------------------------------------------------
    
    def __repr__(self):
        string = ', '.join([ f'{color}={count}' for color, count 
                             in zip(self.colors.keys(), self.colors.values()) 
                            ])
        return f'Hat({string})'
    
    #---METHODS----------------------------------------------------------------
    
    def dict_to_list(self, dic : dict) -> list:
        '''
        Convert a dictionary {'key1' : 1, 'key2' : 3} to a list of key strings
        ['key1', 'key1', 'key2', 'key2', 'key2'].

        Parameters
        ----------
        dic : TYPE
            DESCRIPTION.

        Returns
        -------
        lst : TYPE
            DESCRIPTION.

        '''
        lst = []
        for key, value in zip(dic.keys(), dic.values()):
            lst += [key] * value
        return lst
    
    def draw(self, number : int) -> list:
        '''
        Method to draw a number of balls from the hat without replacement.

        Parameters
        ----------
        number : int
            The number of balls to draw.

        Returns
        -------
        list
            A list of balls drawn by color, e.g. ['red', 'blue', 'red'].
        '''
        try:
            sample = random.sample(self.contents, k=number)
        except ValueError:
            sample = self.contents
        for color in sample:
            self.colors[color] -= 1
            self.contents = self.dict_to_list(self.colors)
        return sample
        
#==============================================================================

def experiment(hat, expected_balls : dict, num_balls_drawn : int, num_experiments : int) -> float:
    '''
    Function to simulate many draws of a fixed amount of balls from a fixed
    distribution or hat.

    Parameters
    ----------
    hat : Hat
        A hat object containing colored balls.
    expected_balls : dict
        A dictionary listing the wanted outcome, e.g. {'red' : 2, 'blue' : 1}.
    num_balls_drawn : int
        The number of balls drawn from the hat without replacement.
    num_experiments : int
        The number of repeat experiments. A higher number will lead to a better
        approximation of the true probablity, as described by the multivariate 
        hypergeometric distribution.

    Returns
    -------
    float
        The experimental probability of pulling said balls from the distribution.
    '''
    success = 0
    for i in range(num_experiments):
        chat = copy.deepcopy(hat)
        result_ = chat.draw(num_balls_drawn)
        result = {}
        for color in result_:
            if color not in result:
                result[color] = 1
            else:
                result[color] += 1
        try:
            if all(result[color] >= expected_balls[color] for color in expected_balls):
                success += 1
        except KeyError:
            pass                 
    return success/num_experiments

#==============================================================================

def mvhgm_fun(hat, expected_balls : dict, num_balls_drawn : int) -> float:
    '''
    A wrapper for `scipy.stats.multivariate_hypergeom` (`see the SciPy 
    documentation <https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.multivariate_hypergeom.html>`_),
    to calculate probabilites for drawing without replacement.

    Parameters
    ----------
    hat : Hat
        A hat object containing colored balls.
    expected_balls : dict
        A dictionary listing the wanted outcome, e.g. {'red' : 2, 'blue' : 1}.
    num_balls_drawn : int
        The number of balls drawn from the hat without replacement.
    
    Returns
    -------
    float
        The experimental probability of pulling said balls from the distribution.
    '''
    sample = list(expected_balls.values())
    population = []
    for color in expected_balls:
        try:
            population.append(hat.colors[color])
        except KeyError:
            return 0
    for color in hat.colors:
        if color not in expected_balls:
            population.append(hat.colors[color])
    
    return multivariate_hypergeom.pmf(x=sample, 
                                      m=population,
                                      n=num_balls_drawn)

#==============================================================================