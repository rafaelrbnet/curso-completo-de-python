from flask import Flask, jsonify
from grupos import grupos
from usuarios import usuarios

app = Flask(__name__)
app.register_blueprint(grupos)
app.register_blueprint(usuarios)


@app.route("/")
def index():
    return "Resposta em Flask"


if __name__ == '__main__':
    app.run(debug=True)
