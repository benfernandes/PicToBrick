import flask
from flask import request, jsonify


def main():
    app = flask.Flask(__name__)
    app.config["DEBUG"] = True

    # Create some test data for our catalog in the form of a list of dictionaries.

    @app.route('/api/v1/maths', methods=['GET'])
    def api_id():
        if 'num' in request.args:
            num = int(request.args['num'])
        else:
            return 'Error: No "num" field provided. Please specify a "num".'

        result = square(num)
        return jsonify(
            {
                'input': num,
                'result': result
            }
        )

    app.run()


def square(number: int) -> int:
    return number * number
