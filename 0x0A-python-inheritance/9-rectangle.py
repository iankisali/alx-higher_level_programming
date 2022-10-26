#!/usr/bin/python3
"""Defines a class Rectangle that inherits from BaseGeometry."""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Subclass Rectangle of BaseGeometry"""
    def __init__(self, width, height):
        """Initialize new Rectangle
        Args:
            width(int): width of rectangle
            height(int): height of rectangle
        """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """calculate area"""
        return self.__width * self.__height

    def __str__(self):
        """print height and width"""
        return '[Rectange] ' + str(self.__width) + "/" + str(self.__height)
