from flask import Flask
from flask import request
from flask import jsonify
import numpy
import sem
app = Flask(__name__)


@app.route('/sem', methods=['POST'])
def semapp():
    obj = request.json
    n = obj['n']
    alpha = obj['alpha']
    sigma = obj['sigma']
    S = obj['S']
    A, Sigma_e = sem.sem(n, alpha, sigma, S)
    result = {
        'alpha': [(i, j, A[i, j]) for i, j in alpha],
        'sigma': [(i, j, Sigma_e[i, j]) for i, j in sigma],
    }
    response = jsonify(result)
    response.headers['Content-Type'] = 'application/json'
    return response


@app.route('/cov', methods=['POST'])
def cov():
    obj = request.json
    result = {
        'data': [[v for v in row] for row in numpy.cov(obj['data'])],
    }
    response = jsonify(result)
    response.headers['Content-Type'] = 'application/json'
    return response


if __name__ == '__main__':
    app.run(debug=True)
