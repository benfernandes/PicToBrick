from math import sqrt
from typing import Tuple

import attr


@attr.s(auto_attribs=True, frozen=True)
class Colour:
    red: int
    green: int
    blue: int

    def diff(self, other: 'Colour') -> float:
        return sqrt(
            pow(self.red - other.red, 2) + pow(self.green - other.green, 2) + pow(self.blue - other.blue, 2)
        )

    def as_rgb(self) -> Tuple[int, int, int]:
        return self.red, self.green, self.blue


@attr.s(auto_attribs=True, frozen=True)
class Shape2D:
    width: int
    height: int


@attr.s(auto_attribs=True, frozen=True)
class Brick:
    colour: Colour
    shape: Shape2D
