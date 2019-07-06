from flask import jsonify
from models.Color import Color


class ColorsController(object):

    @staticmethod
    def get_colors():
        colors = Color.query.all()
        return jsonify(Color.serialize_list(colors))
