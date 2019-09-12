from flask import jsonify

from models import Effect
from templates.Errors import NotFoundError


class EffectController(object):
    @staticmethod
    def index():
        return jsonify(Effect.all())

    @staticmethod
    def post(name: str):
        effect = Effect()
        response = Effect.save(effect)
        print(response)
        return jsonify(response)

    @staticmethod
    def update(name: str):
        segment = Effect.find_effect(name)
        if segment is None:
            raise NotFoundError

    @staticmethod
    def delete(start_pixel: int, end_pixel: int):
        return None