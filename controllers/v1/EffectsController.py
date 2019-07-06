from flask import jsonify
from models.Effect import Effect


class EffectsController(object):

    @staticmethod
    def get_effects():
        effects = Effect.query.all()
        return jsonify(Effect.serialize_list(effects))
