import urllib
from typing import List, Tuple, Set

from PIL import ImageOps, Image

from pic_to_brick.brick import Colour, Brick


class Converter:
    def __init__(self, bricks: List[Brick]):
        self.bricks = bricks

    def convert(self, img_url: str, width: int, height: int) -> str:
        # TODO - Check why this is an unresolved reference
        # noinspection PyUnresolvedReferences
        original_image: Image.Image = Image.open(urllib.request.urlopen(img_url))

        resized_image = self._resize(original_image, width, height)

        coloured_image = self._change_colours(resized_image, self._get_all_colours(self.bricks))
        coloured_image.show()

        return img_url

    @staticmethod
    def _resize(image: Image.Image, width: int, height: int) -> Image.Image:
        size = (width, height)
        return ImageOps.fit(image, size, Image.ANTIALIAS)

    def _change_colours(self, org_image: Image.Image, avail_colours: List[Colour]) -> Image.Image:
        new_image = Image.new('RGB', org_image.size, 0)

        width, height = org_image.size
        for x in range(width):
            for y in range(height):
                pix = org_image.getpixel((x, y))
                r, g, b = pix[0], pix[1], pix[2]

                closest_col = self._closest_colour(Colour(r, g, b), avail_colours)
                new_image.putpixel((x, y), closest_col.as_rgb())

        return new_image

    @staticmethod
    def _get_all_colours(bricks: List[Brick]) -> List[Colour]:
        cols: Set[Colour] = set()

        for brick in bricks:
            col = brick.colour
            if col not in cols:
                cols.add(col)

        return list(cols)

    @staticmethod
    def _closest_colour(pixel_col: Colour, avail_colours: List[Colour]) -> Colour:
        close_colours: List[Tuple[float, Colour]] = []

        for colour in avail_colours:
            close_colours.append((pixel_col.colour_diff(colour), colour))

        close_colours.sort()

        return close_colours[0][1]
