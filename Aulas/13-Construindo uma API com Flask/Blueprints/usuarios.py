from flask import Blueprint, jsonify

usuarios = Blueprint("usuarios", __name__)


@usuarios.route("/usuarios/")
def list_grupos():
    data = {"message": "Aqui serão listados todos os usuarios"}
    return jsonify(data)
