from flask import Blueprint
from app.controllers.auth_controller import login_user, registrar_usuario

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

@auth_bp.route('/login', methods=['POST'])
def login():
    return login_user()

@auth_bp.route('/registro', methods=['POST'])
def registro():
    return registrar_usuario()
