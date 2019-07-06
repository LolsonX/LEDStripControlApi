from flask import Blueprint

from controllers.v1.EffectsController import *
from controllers.v1.ColorsController import *

router = Blueprint('routes', __name__)


@router.route('/v1/colors', methods=['GET'])
def get_colors():
    return ColorsController.get_colors()


@router.route('/v1/effects', methods=['GET'])
def get_effects():
    return EffectsController.get_effects()
