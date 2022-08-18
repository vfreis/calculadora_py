import os
from flask import Flask, request
# from math import sqrt
from calculadora import Calculadora


app = Flask(__name__)

@app.route('/route')
def calculadoraWeb():
    valor1 = request.args.get('v1')
    valor2 = request.args.get('v2')
    operacao = request.args.get('operacao')


    