# TODO Segment model similar to one decribed in ColorControlelr.py

import json

from flask import jsonify

from models.Segment import Segment
from templates.Errors import NotFoundError


class SegmentController(object):
    @staticmethod
    def index():
        return jsonify(Segment.all())

    @staticmethod
    def post(start_pixel: int, end_pixel: int, color: str, effect: str):
        segment = Segment(start_pixel, end_pixel, color, effect)
        response = Segment.save(segment)
        print(response)
        return jsonify(response)

    @staticmethod
    def update(start_pixel: int, end_pixel: int, color: str, effect: str):
        segment = Segment.find_segment(start_pixel, end_pixel)
        if segment is None:
            raise NotFoundError


    @staticmethod
    def delete(start_pixel: int, end_pixel: int):
        return None
