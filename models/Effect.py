import json

from flask import jsonify

from controllers.EffectController import EffectController
from templates.Errors import ModelError


class Effect(object):
    attributes = ['name',
                  'startFromLeft',
                  'secsBeforeNextPixel',
                  'randomizeSegmentColor',
                  'randomizePixelColor',
                  'newColorOnFinish',
                  'randomColorPool',
                  'blinking',
                  'blinkingColors',
                  'insertOtherColors',
                  'colorsToInsert']

    def __init__(self, params: dict):
        for key, value in params.items():
            if key in Effect.attributes:
                self.__setattr__(key, value)
            else:
                raise ModelError(["Param {} not valid for effect".format(key)])

    def to_json(self):
        jsoned = dict()
        for atribute in Effect.attributes:
            jsoned[atribute] = self.__getattribute__(atribute)
        return jsoned

    @staticmethod
    def save(effect):
        effects = Effect.all()
        effect = Effect(effect)
        effects["effects"].append(effect.to_json())
        print(effects)
        Effect.save_changes(effects)
        return effect.to_json()

    @staticmethod
    def update(name: str, params: dict):
        effect = Effect.find_effect(name)
        for key, value in params:
            if key in effect.keys:
                effect[key] = value
            else:
                raise ModelError(["Param {} not valid effect object".format(key)])
        Effect.save(effect)

    @staticmethod
    def all() -> dict:
        with open('resources/effects.json') as effects_db:
            effects: dict = json.loads(effects_db.read())
        return effects

    @staticmethod
    def find_effect(name):
        effects = Effect.all()["effects"]
        return next((effect for effect in effects
                     if effect["name"] == name), None)

    @staticmethod
    def save_changes(effects):
        with open('resources/effects.json', 'w') as effect_db:
            json.dump(effects, effect_db)
