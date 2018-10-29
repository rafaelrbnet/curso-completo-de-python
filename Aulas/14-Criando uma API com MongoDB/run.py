from flask import Flask, jsonify
from usuarios import usuarios

app = Flask(__name__)
app.register_blueprint(usuarios)



@app.route("/")
def index():
    return "Resposta em Flask módulo 14"


if __name__ == '__main__':
    app.run(debug=True)
