import time
from threading import Thread
from flask import jsonify
from models.Color import Color
from app import script_thread


class ColorsController(object):
    script_thread = None

    @staticmethod
    def get_colors():
        # colors = Color.query.all()
        script_thread.start()
        return jsonify({"Test": "test"})

