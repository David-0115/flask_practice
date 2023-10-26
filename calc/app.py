import operations as math

from flask import Flask, request

app = Flask(__name__)

operations = {
    "add": math.add,
    "sub": math.sub,
    "mult": math.mult,
    "div": math.div
}


@app.route('/math/<operation>')
def query_calc(operation):
    a = request.args["a"]
    b = request.args["b"]
    return str(operations[operation](int(a), int(b)))
