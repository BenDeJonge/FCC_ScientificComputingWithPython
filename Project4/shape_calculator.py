# -*- coding: utf-8 -*-
"""
Created on Thu Mar 31 23:19:36 2022

@author: dejong71
"""

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
    
    #---INITIALIZATION---------------------------------------------------------

    def __init__(self, width : int, height : int):
        self.width = width
        self.height = height
    
    #---PROPERTIES-------------------------------------------------------------
    
    @property
    def width(self):
        return self._width
    @width.setter
    def width(self, val : int):
        if isinstance(val, int) and val > 0:
            self._width = val
        else:
            raise ValueError('Width cannot be negative.')
    @width.deleter
    def width(self):
        del self._width

    @property
    def height(self):
        return self._height
    @height.setter
    def height(self, val : int):
        if isinstance(val, int) and val > 0:
            self._height = val
        else:
            raise ValueError('Height cannot be negative.')
    @height.deleter
    def height(self):
        del self._height
        
    #---REPRESENTATION---------------------------------------------------------
    
    def __repr__(self):
        return f'Rectangle(width={self.width}, height={self.height})'
    
    #---SETTERS----------------------------------------------------------------
    # In practice replaced by PROPERTIES, but required for unittests.
    def _check_val(self, val):
        return isinstance(val, int) and val > 0
    
    def set_width(self, val : int):
        '''
        Set the Rectangle width to any integer value.
        '''
        if self._check_val(val):
            self.width = val
            
    def set_height(self, val):
        '''
        Set the Rectangle height to any integer value.
        '''
        if self._check_val(val):
            self.height = val
    
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
    
    #---INITIALIZATION---------------------------------------------------------
    
    def __init__(self, side : int):
        self.width = side
        self.height = side
        
    #---REPRESENTATION---------------------------------------------------------
    
    def __repr__(self):
        return f'Square(side={self.width})'
    
    #---SETTERS----------------------------------------------------------------
    # In practice replaced by PROPERTIES, but required for unittests.
    def set_width(self, val):
        '''
        Set the Square width and height to any integer value.
        '''
        if self._check_val(val):
            self.width = val
            self.height = val
            
    def set_height(self, val):
        '''
        Set the Square width and height to any integer value.
        '''
        if self._check_val(val):
            self.width = val
            self.height = val      
            
    def set_side(self, val):
        '''
        Set the Square width and height to any integer value.
        '''
        if self._check_val(val):
            self.width = val
            self.height = val  
            
#==============================================================================