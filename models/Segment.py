import json

from flask import jsonify

from controllers.ColorController import ColorController
from models.JsonModel import JsonModel
from templates.Errors import ModelError


class Segment(JsonModel):

    required_attributes = ['start_pixel', 'end_pixel', 'color', 'effect']

    def __init__(self):
        self.initialize()
    # def __init__(self, start_pixel: int, end_pixel: int, color: str, effect: str):
    #     self.start_pixel: int = start_pixel
    #     self.end_pixel: int = end_pixel
    #     self.color: str = color
    #     self.effect: str = effect
    #
    # def to_json(self):
    #     return {"start_pixel": self.start_pixel,
    #             "end_pixel": self.end_pixel,
    #             "color": self.color,
    #             "effect": self.effect}
    #
    # @staticmethod
    # def save(segment):
    #     Segment.validate_segment(segment.start_pixel, segment.end_pixel, segment.color, segment.effect)
    #     segments = Segment.all()
    #     segments["segments"].append(segment.to_json())
    #     print(segments)
    #     Segment.save_changes(segments)
    #     return segment.to_json()
    #
    # @staticmethod
    # def update(start_pixel, end_pixel, color, effect):
    #     Segment.validate_segment(start_pixel, end_pixel, color, effect)
    #
    # @staticmethod
    # def all() -> dict:
    #     with open('resources/segments.json') as segments_db:
    #         segments: dict = json.loads(segments_db.read())
    #     return segments
    #
    # @staticmethod
    # def find_segment(start_pixel, end_pixel) -> dict:
    #     segments = Segment.all()["segments"]
    #     return next((segment for segment in segments
    #                  if segment["start_pixel"] == start_pixel and
    #                  segment["end_pixel"] == end_pixel), None)
    #
    # @staticmethod
    # def save_changes(segments):
    #     with open('resources/segments.json', 'w') as segment_db:
    #         json.dump(segments, segment_db)
    #
    # @staticmethod
    # def validate_segment(start_pixel, end_pixel, color, effect) -> bool:
    #     errors = []
    #     segment = Segment.find_segment(start_pixel, end_pixel)
    #     if segment is not None:
    #         errors.append("Segment already exists")
    #     else:
    #         color = ColorController.find_color(color)
    #         if color is None:
    #             errors.append("Color not found")
    #     if len(errors) == 0:
    #         return True
    #     raise ModelError(errors)

print(Segment.all())