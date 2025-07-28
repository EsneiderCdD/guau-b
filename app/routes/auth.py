from flask import Blueprint, request, jsonify
from app.controllers.auth_controller import login_user

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

@auth_bp.route('/login', methods=['POST'])
def login():
    return login_user()
