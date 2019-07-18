from typing import Set, Type, List, Tuple

import attr
from math import sqrt

bricks: Set[Type['Brick']] = set()


def get_all_colours() -> List['Colour']:
    return [brick.colour for brick in bricks]


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

    def as_rgb(self) -> Tuple[int, int, int]:
        return self.red, self.green, self.blue


@attr.s(auto_attribs=True)
class Shape2D:
    width: int
    height: int


@attr.s(auto_attribs=True)
class Brick:
    colour: Colour
    shape: Shape2D

    def __init_subclass__(cls, **kwargs):
        if cls not in bricks:
            bricks.add(cls)


class RedBrick(Brick):
    colour = Colour(255, 0, 0)
    shape = Shape2D(1, 1)


class YellowBrick(Brick):
    colour = Colour(255, 255, 0)
    shape = Shape2D(1, 1)


class GreenBrick(Brick):
    colour = Colour(0, 255, 0)
    shape = Shape2D(1, 1)


class TealBrick(Brick):
    colour = Colour(0, 255, 255)
    shape = Shape2D(1, 1)


class BlueBrick(Brick):
    colour = Colour(0, 0, 255)
    shape = Shape2D(1, 1)


class PinkBrick(Brick):
    colour = Colour(255, 0, 255)
    shape = Shape2D(1, 1)


class BlackBrick(Brick):
    colour = Colour(0, 0, 0)
    shape = Shape2D(1, 1)


class WhiteBrick(Brick):
    colour = Colour(255, 255, 255)
    shape = Shape2D(1, 1)
