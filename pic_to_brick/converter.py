from PIL import ImageOps, Image


class Converter:
    def convert(self, img_url: str, width: int, height: int) -> str:
        # TODO - Check why this is an unresolved reference
        # noinspection PyUnresolvedReferences
        original_image: Image.Image = Image.open(urllib.request.urlopen(img_url))
        resized_image = self.resize(original_image, width, height)

        resized_image.show()

        return img_url

    @staticmethod
    def resize(image: Image.Image, width: int, height: int) -> Image.Image:
        size = (height, width)
        return ImageOps.fit(image, size, Image.ANTIALIAS)
