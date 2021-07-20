from flask import Flask, jsonify, request
import json

from jinja2.utils import Joiner

from data.developers import DEVS


app = Flask(__name__)

# Receiving all data(GET) and including a new data(POST)
@app.route('/dev', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        response = DEVS
    
    else:
        if request.method == 'POST':
            new_data = json.loads(request.data)
            position = len(DEVS)
            new_data['id'] = position
            DEVS.append(new_data)
            response = {
                'status': 'sucess', 
                'message': f'id {position} record successfully added'}

    return jsonify(response)

# Receiving(GET), Updating(PUT), Deleting(DELETE) datas
@app.route('/dev/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def developers(id):
    if request.method == 'GET':
        try:
            response = DEVS[id]

        except IndexError:
            message = f'id {id} data does not exist'
            response = {'status': 'error', 'message': message}

        except Exception:
            message = f'data not found'
            response = {'status': 'error', 'message': message}

        return jsonify(response)

    
    elif request.method == 'PUT':
        response = json.loads(request.data)   
        DEVS[id] = response
        return jsonify(response)
    
    elif request.method == 'DELETE':
        DEVS.pop(id)
        return jsonify({'message': 'deleted data'})


if __name__ == '__main__':
    app.run(debug=True)