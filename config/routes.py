from flask import Blueprint, jsonify, abort, request
from werkzeug.exceptions import HTTPException
from controllers.ColorController import ColorController
from controllers.SegmentsController import SegmentController
from templates.Errors import ModelError, NotFoundError

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
    return color


def delete_color(color_name):
    color = ColorController.delete(color_name)
    return color


def create_color(color_name, red, green, blue):
    color = ColorController.post(color_name, red, green, blue)
    return color


@router.route('/segments', methods=["GET", "POST"])
def segments():
    if request.method == "GET":
        return index_segments()
    if request.method == "POST":
        params = request.get_json()
        return create_segment(params["start_pixel"], params["end_pixel"], params["color"], params["effect"])


def index_segments():
    return SegmentController.index()


def create_segment(start_pixel, end_pixel, color, effect):
    return SegmentController.post(start_pixel, end_pixel, color, effect)


@router.errorhandler(ModelError)
def invalid_model(error):
    return render_error(error)


@router.errorhandler(NotFoundError)
def invalid_model(error):
    return render_error(error)


def render_error(error: HTTPException):
    response = jsonify(error.description)
    response.status_code = error.code
    return response
