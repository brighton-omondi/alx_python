#!/usr/bin/python3
""" Rectangle module """
from models.base import Base


class Rectangle(Base):
    """ Rectangle class, inherits from Base """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Class constructor """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

        # ... (other methods and attributes)

    def area(self):
        """ Calculate and return the area of the rectangle """
        return self.__width * self.__height

    # ... (other methods and attributes)

    # ... (other methods and attributes)

    def display(self):
        """ Display the Rectangle instance using '#' characters """
        for _ in range(self.__height):
            print('#' * self.__width)

    # ... (other methods and attributes)

    # ... (other methods and attributes)

    def __str__(self):
        """ Return a string representation of the Rectangle instance """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height
        )

    # ... (other methods and attributes)

    # ... (other methods and attributes)

    def display(self):
        """ Display the Rectangle instance using '#' characters """
        for _ in range(self.__y):
            print()
        for _ in range(self.__height):
            print(' ' * self.__x + '#' * self.__width)

    # ... (other methods and attributes)

    # ... (other methods and attributes)

    def update(self, *args):
        """ Update the attributes of the Rectangle instance """
        if args:
            attributes = ["id", "width", "height", "x", "y"]
            for i, value in enumerate(args):
                setattr(self, attributes[i], value)

    # ... (other methods and attributes)

    # ... (other methods and attributes)

    def update(self, *args, **kwargs):
        """ Update the attributes of the Rectangle instance """
        if args:
            attributes = ["id", "width", "height", "x", "y"]
            for i, value in enumerate(args):
                setattr(self, attributes[i], value)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    # ... (other methods and attributes)

    @property
    def width(self):
        """ Getter for width attribute """
        return self.__width

    @width.setter
    def width(self, value):
        """ Setter for width attribute """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ Getter for height attribute """
        return self.__height

    @height.setter
    def height(self, value):
        """ Setter for height attribute """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ Getter for x attribute """
        return self.__x

    @x.setter
    def x(self, value):
        """ Setter for x attribute """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ Getter for y attribute """
        return self.__y

    @y.setter
    def y(self, value):
        """ Setter for y attribute """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value
