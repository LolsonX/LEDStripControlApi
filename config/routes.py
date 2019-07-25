from flask import Blueprint, jsonify, abort, request
from controllers.ColorController import ColorController
from templates.Errors import ModelError

router = Blueprint('routes', __name__)


@router.route('/colors', methods=["GET", "POST"])
def colors():
    if request.method == "GET":
        return index_colors()
    if request.method == "POST":
        params = request.get_json()
        return create_color(params["color_name"], params["red"], params["green"], params["blue"])


def index_colors():
    return ColorController.index()


@router.route('/colors/<string:color_name>', methods=["GET", "DELETE"])
def color_operations(color_name):
    if request.method == "GET":
        return show_color(color_name)
    if request.method == "DELETE":
        return delete_color(color_name)


def show_color(color_name):
    color = ColorController.show(color_name)
    if color is not None:
        return color
    abort(404)


def delete_color(color_name):
    color = ColorController.delete(color_name)
    if color is not None:
        return color
    abort(404)


def create_color(color_name, red, green, blue):
    color = ColorController.post(color_name, red, green, blue)
    return color


@router.errorhandler(404)
def not_found(error):
    response = jsonify({
        'status': 404,
        'message': 'Not found'
    })
    response.status_code = 404
    return response


@router.errorhandler(ModelError)
def invalid_model(error):
    response = jsonify(error.description)
    response.status_code = 422
    return response, getattr(error, 'code', 422)
