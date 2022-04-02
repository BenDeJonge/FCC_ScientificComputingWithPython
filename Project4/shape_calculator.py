# -*- coding: utf-8 -*-
"""
Created on Thu Mar 31 23:19:36 2022

@author: dejong71
"""

#==============================================================================

class PositiveIntegerDescriptor: 
    '''
    A descriptor class to enforce an attribute to be a strictly positive integer.

    Parameters
    ----------
    name : str
        The public name of the attribute.

    Returns
    -------
    None.
    '''
    
    #--INITIALIZATION----------------------------------------------------------
    
    def __init__(self, name : str):
        self.public_name  = name
        self.private_name = '_' + name
            
    #--GETTERS AND SETTERS-----------------------------------------------------

    def __get__(self, obj, objtype=None):
        return getattr(obj, self.private_name)

    def __set__(self, obj, new_value):
        if isinstance(new_value, int) and new_value > 0:
            setattr(obj, self.private_name, new_value)
        else:
            raise ValueError(f'{self.public_name.capitalize()} must be a strictly positive integer.')

#==============================================================================

class Rectangle:
    '''
    A simple class to model a rectangle.

    Parameters
    ----------
    width : int
        The width of the rectangle.
    height : int
        The height of the rectangle.

    Returns
    -------
    None.
    '''
    
    #---DESCRIPTORS------------------------------------------------------------
    
    width = PositiveIntegerDescriptor('width')
    height = PositiveIntegerDescriptor('height')
    
    #---INITIALIZATION---------------------------------------------------------

    def __init__(self, width : int, height : int):
        self.width  = width
        self.height = height
        
    #---REPRESENTATION---------------------------------------------------------
    
    def __repr__(self):
        return f'Rectangle(width={self.width}, height={self.height})'
    
    #---SETTERS----------------------------------------------------------------
    
    def set_width(self, value : int):
        '''
        Set the Rectangle width to any stricly positive integer value.
        '''
        self.width = value
            
    def set_height(self, value):
        '''
        Set the Rectangle height to any stricly positive integer value.
        '''
        self.height = value
    
    #---GEOMETRIC METHODS------------------------------------------------------
    
    def get_area(self):
        '''
        Get the area by multiplying width and height.
        '''
        return self.width * self.height
    
    def get_perimeter(self):
        '''
        Get the perimeter by adding all sides.
        '''
        return 2 * self.width + 2 * self.height
    
    def get_diagonal(self):
        '''
        Get the diagonal using the Pythagorem theorem.
        '''
        return (self.width ** 2 + self.height ** 2) ** 0.5
    
    #---GRAPHICAL METHODS------------------------------------------------------

    def get_picture(self, limit : int=50):
        '''
        Get a string representation of the shape, composed out of *s. Output 
        will only be generated if both dimensions are below the limit.

        Parameters
        ----------
        limit : int, optional
            The maximal dimensions of the shape where a picture is still 
            generated. The default is 50.

        Returns
        -------
        str
            A string representation of the shape, composed out of *s.
        '''
        if any([self.width > limit, self.height > limit]):
            return 'Too big for picture.'
        else:
            return f'{self.width * "*"}\n' * self.height
    
    def get_amount_inside(self, other):
        if isinstance(other, Rectangle):
            return (self.width // other.width) * (self.height // other.height)
        
#==============================================================================

class Square(Rectangle):
    '''
    A simple class to model a square.

    Parameters
    ----------
    side : int
        The side of the square.

    Returns
    -------
    None.
    '''
    
    #---DESCRIPTORS------------------------------------------------------------
    
    width = PositiveIntegerDescriptor('width')
    height = PositiveIntegerDescriptor('height')
    
    #---INITIALIZATION---------------------------------------------------------
    
    def __init__(self, side : int):
        self.width  = side
        self.height = side
        
    #---REPRESENTATION---------------------------------------------------------
    
    def __repr__(self):
        return f'Square(side={self.width})'
    
    #---SETTERS----------------------------------------------------------------
    # In practice replaced by PROPERTIES, but required for unittests.
    def set_width(self, value):
        '''
        Set the Square width and height to any stricly positive integer value.
        '''
        self.width  = value
        self.height = value
            
    def set_height(self, value):
        '''
        Set the Square width and height to any stricly positive integer value.
        '''
        self.width  = value
        self.height = value
            
    def set_side(self, value):
        '''
        Set the Square width and height to any stricly positive integer value.
        '''
        self.width  = value
        self.height = value

#==============================================================================