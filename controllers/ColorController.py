# TODO Create model for colors which will store list of colors and do all operations on it

import json

from flask import jsonify
from templates.Errors import ModelError, NotFoundError


class ColorController(object):
    @staticmethod
    def index():
        colors = ColorController.load_colors_list()
        return jsonify(colors["colors"])

    @staticmethod
    def show(color_name):
        color = ColorController.find_color(color_name)
        if color is not None:
            return jsonify(color)
        raise NotFoundError("Color")

    @staticmethod
    def post(color_name, red=-1, green=-1, blue=-1):
        ColorController.validate_color(color_name, red, green, blue)
        color = {"name": color_name, "red": red, "green": green, "blue": blue}
        colors = ColorController.load_colors_list()
        colors["colors"].append(color)
        ColorController.save_changes(colors)
        return jsonify(color)

    @staticmethod
    def update(color_name, red, green, blue):
        ColorController.validate_color(color_name, red, green, blue)
        colors = ColorController.load_colors_list()
        color = {"name": color_name, "red": red, "green": green, "blue": blue}
        colors["colors"].append(color)
        ColorController.save_changes(colors)

    @staticmethod
    def delete(color_name):
        colors = ColorController.load_colors_list()
        for color in colors["colors"]:
            if color["name"] == color_name:
                colors["colors"].remove(color)
                ColorController.save_changes(colors)
                return jsonify(color)
        raise NotFoundError("Color")

    @staticmethod
    def load_colors_list() -> dict:
        with open('resources/colors.json') as color_db:
            colors = json.loads(color_db.read())

        return colors

    @staticmethod
    def find_color(color_name):
        colors = ColorController.load_colors_list()["colors"]
        return next((color for color in colors if color["name"] == color_name), None)

    @staticmethod
    def save_changes(colors):
        with open('resources/colors.json', 'w') as color_db:
            json.dump(colors, color_db)

    @staticmethod
    def validate_color(name: str, red: int, green: int, blue: int) -> bool:
        color = ColorController.find_color(name)
        errors = []
        if color is not None:
            errors.append("Name already exists")
        if red > 255 or red < 0:
            errors.append("Red value incorrect")
        if green > 255 or green < 0:
            errors.append("Green value incorrect")
        if blue > 255 or blue < 0:
            errors.append("Blue value incorrect")
        if len(errors) == 0:
            return True
        raise ModelError(errors)


