#!/usr/bin/python3
"""Defines a class MyInt that inherits from int."""


class MyInt(int):
    """invert int operator == and != """

    def __eq__(self, value):
        """ovrride =="""
        return self.real != value

    def __ne__(self, value):
        """override !="""
        return self.real == value
