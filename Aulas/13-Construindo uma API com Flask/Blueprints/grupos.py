from flask import Blueprint, jsonify

grupos = Blueprint("grupos", __name__)


@grupos.route("/grupos/")
def list_grupos():
    data = {"message": "Aqui serão listados todos os grupos"}
    return jsonify(data)
