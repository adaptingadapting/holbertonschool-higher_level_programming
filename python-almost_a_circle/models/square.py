#!/usr/bin/python3
""" module that defines square class """

from models.rectangle import Rectangle


class Square(Rectangle):
    """ square class has methods and attributes :) """

    def __init__(self, size, x=0, y=0, id=None):
        """ docu """

        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ docu """

        return self.width

    @size.setter
    def size(self, value):
        """ docu """

        self.width = value
        self.height = value

    def __str__(self):
        """ docu """

        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"

    def update(self, *args, **kwargs):
        """ docu """

        if args and len(args) != 0:
            i = 0
            for arg in args:
                if i == 0:
                    self.id = arg
                if i == 1:
                    self.size = arg
                if i == 2:
                    self.x = arg
                if i == 3:
                    self.y = arg
                i += 1
        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "size":
                    self.size = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value

    def to_dictionary(self):
        """ docu """

        return dict(id=self.id, x=self.x, size=self.size, y=self.y)
