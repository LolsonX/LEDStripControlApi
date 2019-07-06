from app import db
from serializer import Serializer


class Color(db.Model, Serializer):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), unique=True, nullable=False)
    red = db.Column(db.SmallInteger, unique=False, nullable=False)
    green = db.Column(db.SmallInteger, unique=False, nullable=False)
    blue = db.Column(db.SmallInteger, unique=False, nullable=False)

    def serialize(self):
        d = Serializer.serialize(self)
        return d

