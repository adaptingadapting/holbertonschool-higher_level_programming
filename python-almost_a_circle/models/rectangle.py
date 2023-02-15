#!/usr/bin/python3
""" python 3 creating a module class """


from models.base import Base


class Rectangle(Base):
    """ defines a rectangle class """

    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
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
        if not type(value) is int:
            raise TypeError("width must be an integer")
        if not value > 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @height.setter
    def height(self, value):
        if not type(value) is int:
            raise TypeError("height must be an integer")
        if not value > 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @x.setter
    def x(self, value):
        if not type(value) is int:
            raise TypeError("x must be an integer")
        if not value >= 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        if not type(value) is int:
            raise TypeError("y must be an integer")
        if not value >= 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        return self.__height * self.__width

    def display(self):
        for k in range(self.__y):
            print()
        for i in range(self.__height):
            for w in range(self.__x):
                print(" ", end="")
            for j in range(self.__width):
                print("#", end="")
            if i < self.__height:
                print()

    def __str__(self):
        return f"[Rectangle] ({self.id}) {self.__x}/{self.__y}\
 - {self.__width}/{self.__height}"

    def update(self, *args, **kwargs):
        if args and len(args) != 0:
            i = 0
            for arg in args:
                if i == 0:
                    self.id = arg
                if i == 1:
                    self.__width = arg
                if i == 2:
                    self.__height = arg
                if i == 3:
                    self.__x = arg
                if i == 4:
                    self.__y = arg
                i += 1
        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "width":
                    self.__width = value
                if key == "height":
                    self.__height = value
                if key == "x":
                    self.__x = value
                if key == "y":
                    self.__y = value

    def to_dictionary(self):
        return dict(x=self.x, y=self.y, id=self.id, height=self.height,
                    width=self.width)
