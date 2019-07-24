from app import db
from serializer import Serializer


class StripConfig(db.Model, Serializer):

    id = db.Column(db.Integer, primary_key=True)
    leds_per_meter = db.Column(db.SmallInteger, unique=False, nullable=False)
    strip_length = db.Column(db.SmallInteger, unique=False, nullable=False)
    gpio_number = db.Column(db.SmallInteger, unique=False, nullable=False)
    brightness = db.Column(db.Float, unique=False, nullable=False)

    def serialize(self):
        d = Serializer.serialize(self)
        return d
