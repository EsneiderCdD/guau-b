from flask import Blueprint
from app.controllers.perros_controller import get_perros

perros_bp = Blueprint('perros', __name__, url_prefix='/perros')

@perros_bp.route('/', methods=['GET'])
def listar_perros():
    return get_perros()
