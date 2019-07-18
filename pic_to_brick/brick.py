import attr
from math import sqrt


@attr.s(auto_attribs=True)
class Colour:
    red: int
    green: int
    blue: int

    def colour_diff(self, other) -> float:
        return sqrt(
            pow(self.red - other.red, 2) +
            pow(self.green - other.green, 2) +
            pow(self.blue - other.blue, 2)
        )


@attr.s(auto_attribs=True)
class Shape2D:
    width: int
    height: int


@attr.s(auto_attribs=True)
class Brick:
    colour: Colour
    shape: Shape2D


class RedBrick(Brick):
    colour = Colour(255, 0, 0)
    shape = Shape2D(1, 1)
