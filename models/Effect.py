from app import db
from serializer import Serializer


class Effect(db.Model, Serializer):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), unique=True, nullable=False)
    time_period = db.Column(db.Integer, nullable=True)

    def serialize(self):
        d = Serializer.serialize(self)
        return d

