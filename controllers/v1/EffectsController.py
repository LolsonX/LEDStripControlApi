from flask import jsonify

from app import script_thread
from models.Effect import Effect


class EffectsController(object):

    @staticmethod
    def get_effects():
        # effects = Effect.query.all()
        script_thread.stop()
        return jsonify({"Test12": "test2"})
