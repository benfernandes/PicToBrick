from typing import List, Set, Tuple
from urllib.request import urlopen

from PIL import Image, ImageOps

from pic_to_brick.brick import Brick, Colour


class Converter:
    def __init__(self, bricks: Set[Brick]):
        self.bricks = bricks

    def convert(self, img_url: str, width: int, height: int) -> str:
        original_image: Image.Image = Image.open(urlopen(img_url))
        original_image = original_image.convert('RGB')
        resized_image = self._resize(original_image, width, height)
        coloured_image = self._change_colours(resized_image, self._get_all_colours(self.bricks))

        coloured_image.show()

        return img_url

    @staticmethod
    def _resize(image: Image.Image, width: int, height: int) -> Image.Image:
        size = (width, height)
        return ImageOps.fit(image, size)

    def _change_colours(self, org_image: Image.Image, avail_colours: Set[Colour]) -> Image.Image:
        new_image = Image.new('RGB', org_image.size, 0)

        width, height = org_image.size
        for x in range(width):
            for y in range(height):
                pix = org_image.getpixel((x, y))
                closest_col = self._closest_colour(Colour(pix[0], pix[1], pix[2]), avail_colours)
                new_image.putpixel((x, y), closest_col.as_rgb())

        return new_image

    @staticmethod
    def _get_all_colours(bricks: Set[Brick]) -> Set[Colour]:
        return {brick.colour for brick in bricks}

    @staticmethod
    def _closest_colour(pixel_col: Colour, avail_colours: Set[Colour]) -> Colour:
        close_colours: List[Tuple[float, Colour]] = []

        for colour in avail_colours:
            close_colours.append((pixel_col.diff(colour), colour))

        close_colours.sort()

        return close_colours[0][1]
