from flask import jsonify
from werkzeug.exceptions import HTTPException


class ModelError(HTTPException):

    def __init__(self, message: list):
        super().__init__()
        self.message = message
        self.code = 422
        self.description = {"errors": self.message, "status": self.code}


class NotFoundError(HTTPException):

    def __init__(self, object_name: str):
        super().__init__()
        self.code = 404
        self.description = {"errors": "Not found {}".format(object_name)}
