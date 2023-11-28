#!/usr/bin/python3
"""
This is a "Rectangle" module.

Rectangle has public class attribute number_of_instances
Rectangle has public attribute print_symbol for representation
This module defines a simple rectangle by an integer width and height
Default width and height are 0, and raises errors on invalid input
Methods getter and setter for width and height attributes
Method area that returns area of the rectangle
Method perimeter that returns perimeter of the rectangle
Magic methods __str__ and __repr__ handling
Method Print a message when an instance is deleted
Static Method bigger_or_equal returns biggest rectangle based on area
Class Method square that returns a rectangle with width = height = size.
"""


class Rectangle:
    """A Recyangle class defined by its width and height."""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Initialize a new rectangle.

        Args:
            width (int): width of the rectangle.
            height (int): height of the rectangle.
        """
        Rectangle.number_of_instances += 1
        self.height = height
        self.width = width

    @property
    def width(self):
        """Getter for width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for width."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter for height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for height."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Method that returns area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Method that returns perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Returns a string represented by symbol in print_symbol"""
        if self.__width == 0 or self.__height == 0:
            return ""
        else:
            for i in range(0, self.__height):
                try:
                    print(str(self.print_symbol) * self.__width, end='')
                except Exception:
                    print(type(self).print_symbol * self.__width, end ='')
                if i is not self.__height - 1:
                    print("")
            return ""

    def __repr__(self):
        """Returns a string representation of a rectangle"""
        str_w = str(self.__width)
        str_h = str(self.__height)
        return "Rectangle(" + str_w + ", " + str_h + ")"

    def __del__(self):
        """Prints a message when an instance is deleted"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Returns the biggest rectangle based on the area"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_2.area() > rect_1.area():
            return rect_2
        else:
            return rect_1

    @classmethod
    def square(cls, size=0):
        """Returns a rectangle with width = height = size"""
        return cls(size, size)
