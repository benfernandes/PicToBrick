from typing import Dict

import flask
from flask import request, jsonify

# Example image
# https://upload.wikimedia.org/wikipedia/commons/thumb/e/e5/NASA_logo.svg/320px-NASA_logo.svg.png?1563390243451
# https://bit.ly/32rGl1v
from pic_to_brick.converter import Converter
from pic_to_brick.exceptions import ArgumentError


def main():
    app = flask.Flask(__name__)

    # app.config["DEBUG"] = True

    @app.route('/api/v1/test', methods=['GET'])
    def test():
        return f'{app.config["DEBUG"]}'

    @app.route('/api/v1/convert', methods=['GET'])
    def api_id():
        required_args = {
            'img_url': str,
            'height': int,
            'width': int
        }

        try:
            args = check_args(required_args, request.args)
        except ArgumentError as err:
            return err

        out_img_url = Converter().convert(args['img_url'], args['width'], args['height'])

        return jsonify(
            {
                'input_img_url': args['img_url'],
                'height': args['height'],
                'width': args['width'],
                'output_img_url': out_img_url
            }
        )

    # Visible across the network
    # app.run(host='0.0.0.0')

    # Locked to this machine only
    app.run()


def check_args(required_args, request_args) -> Dict:
    args = {}

    for arg in required_args.keys():
        try:
            args[arg] = required_args[arg]
        except KeyError:
            raise ArgumentError(arg)

    return args
