#!/usr/bin/python3
""" python 3 creating a module class """

from models.base import Base

class Rectangle(Base):
    """ defines a rectangle class """

    def __init__(self, width, height, x=0, y=0, id=None):
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property

    def width(self):
        return self.__width

    @property

    def height(self):
        return self.__height

    @property

    def x(self):
        return self.__x

    @property

    def y(self):
        return self.__y

    @width.setter

    def width(self, value):
        self.__width = value

    @height.setter

    def height(self, value):
        self.__height = value

    @x.setter

    def x(self, value):
        self.__x = value

    @y.setter

    def y(self, value):
        self.__y = value
