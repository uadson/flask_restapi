# 2. Returning JSON elements

from flask import Flask, jsonify, request
import json


app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello Dev'


@app.route('/<int:id>')
def person(id):
    return jsonify(
        {'id': id,
         'name': 'uadson',
         'ocupation': 'developer',   
        })

@app.route('/add/<int:value1>/<int:value2>')
def add(value1, value2):
    sum = value1 + value2

    return jsonify({'sum': sum})


@app.route('/values', methods=['POST', 'GET'])
def values():
    if request.method == 'POST':
        # receiving data as string
        # data = {'values': [10, 20, 30, 40]}
        
        value_list = request.data
        
        # receivind data as string and converting to JSON
        value_list = json.loads(request.data)

        # returning the sum of values from the list
        total = sum(value_list['values'])

    elif request.method == 'GET':
        total = 0
    
    return jsonify({'total_sum': total})


if __name__ == '__main__':
    app.run(debug=True)