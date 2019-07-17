import urllib

import flask
from PIL import Image, ImageOps
from flask import request, jsonify


# Example image
# https://upload.wikimedia.org/wikipedia/commons/thumb/e/e5/NASA_logo.svg/320px-NASA_logo.svg.png?1563390243451
# https://bit.ly/32rGl1v
def main():
    app = flask.Flask(__name__)
    # app.config["DEBUG"] = True

    @app.route('/api/v1/test', methods=['GET'])
    def test():
        return f'<h1>{app.config["DEBUG"]}</h1>'

    @app.route('/api/v1/convert', methods=['GET'])
    def api_id():
        print(app.config['DEBUG'])
        if 'img_url' in request.args:
            in_img_url = str(request.args['img_url'])
        else:
            return 'Error: No "img_url" field provided. Please specify a "img_url".'

        if 'height' in request.args:
            height = int(request.args['height'])
        else:
            return 'Error: No "height" field provided. Please specify a "height".'

        if 'width' in request.args:
            width = int(request.args['width'])
        else:
            return 'Error: No "width" field provided. Please specify a "width".'

        out_img_url = convert(in_img_url, height, width)

        return jsonify(
            {
                'input_img_url': in_img_url,
                'height': height,
                'width': width,
                'output_img_url': out_img_url
            }
        )

    # NOTE - Set to use machine IP address
    app.run(host='0.0.0.0')


def convert(img_url: str, height: int, width: int) -> str:
    # TODO - Check why this is an unresolved reference
    # noinspection PyUnresolvedReferences
    original_image: Image.Image = Image.open(urllib.request.urlopen(img_url))
    resized_image = resize(original_image, height, width)

    resized_image.show()

    return img_url


def resize(image: Image.Image, height: int, width: int) -> Image.Image:
    size = (height, width)
    return ImageOps.fit(image, size, Image.ANTIALIAS)
