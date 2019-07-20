from typing import Dict, List, Set, cast

import flask
from flask import request, jsonify

# Example image
# https://upload.wikimedia.org/wikipedia/commons/thumb/e/e5/NASA_logo.svg/320px-NASA_logo.svg.png?1563390243451
# https://bit.ly/32rGl1v

from pic_to_brick.brick import Brick, Colour, Shape2D
from pic_to_brick.converter import Converter
from pic_to_brick.database.db_connection import DbSessionFactory
from pic_to_brick.database.query_runner import QueryRunner, AllBricksQuery
from pic_to_brick.exceptions import ArgumentError


class Main:
    def __init__(self):
        db_session_factory = DbSessionFactory('')
        query_runner = QueryRunner(db_session_factory)
        all_bricks = cast(Set[Brick], query_runner.run_query(AllBricksQuery()))
        self.converter = Converter(all_bricks)

    def run(self):

        app = flask.Flask(__name__)
        app.config["DEBUG"] = True

        @app.route('/api/v1/test', methods=['GET'])
        def test():
            return f'{app.config["DEBUG"]}'

        @app.route('/api/v1/convert', methods=['GET'])
        def api_id():
            required_args = {
                'img_url': str,
                'width': int,
                'height': int
            }

            try:
                args = self._check_args(required_args, dict(request.args))
            except ArgumentError as err:
                return err

            out_img_url = self.converter.convert(args['img_url'], args['width'], args['height'])

            return jsonify(
                {
                    'input_img_url': args['img_url'],
                    'width': args['width'],
                    'height': args['height'],
                    'output_img_url': out_img_url
                }
            )

        # Visible across the network
        # app.run(host='0.0.0.0')

        # Locked to this machine only
        app.run()

    @staticmethod
    def _get_all_bricks() -> List[Brick]:
        # TODO - PTB-3 - Use database here instead
        return [
            Brick(
                Colour(111, 12, 43),
                Shape2D(2, 2)
            ),
            Brick(
                Colour(235, 104, 33),
                Shape2D(1, 4)
            )
        ]

    @staticmethod
    def _check_args(required_args, request_args) -> Dict:
        args = {}

        for arg, fun in required_args.items():
            try:
                args[arg] = fun(request_args[arg])
            except KeyError:
                raise ArgumentError(arg)

        return args
