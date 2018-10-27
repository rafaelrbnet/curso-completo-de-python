#!/usr/bin/python
# -*- coding: UTF-8 -*-
# flask_application.py

# Importação dos módulos
from flask import Flask

app = Flask(__name__)


@app.route("/")
# Chamando a função principal
def hello():
    return "Ola Mundo!"


if __name__ == '__main__':
    app.run(debug=True)
