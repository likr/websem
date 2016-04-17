from flask import Flask
from flask import request
from flask import jsonify
from flask.ext.cors import CORS
import numpy
import sem

app = Flask(__name__)
CORS(app)

@app.route('/sem', methods=['POST'])
def semapp():
    obj = request.json
    n = obj['n']
    alpha = obj['alpha']
    sigma = obj['sigma']
    sigma_fixed = obj['sigma_fixed'] if 'sigma_fixed' in obj else []
    S = obj['S']
    A, Sigma_e, gfi = sem.sem(n, alpha, sigma, S, sigma_fixed)
    result = {
        'alpha': [(i, j, A[i, j]) for i, j in alpha],
        'sigma': [(i, j, Sigma_e[i, j]) for i, j in sigma],
        'GFI': gfi,
        'attributes': [
            {
                'name': 'GFI',
                'value': gfi
            }
        ],
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
