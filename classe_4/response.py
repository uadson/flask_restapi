from flask import Flask, request, jsonify
import json

from data.tasks import TASKS


app = Flask(__name__)

# list all tasks (method=GET) or add a new task (method=POST)
@app.route('/tasks', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        response = TASKS

    else:
        if request.method == 'POST':
            new_data = json.loads(request.data)
            position = len(TASKS)
            new_data['id'] = position
            TASKS.append(new_data)
            response = {
                'status': 'success',
                'message': f'id {position} record successfully added',
            }

    return jsonify(response)


#list task by id(GET), update task by id(PUT)
@app.route('/tasks/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def task(id):
    if request.method == 'GET':
        try:
           response = TASKS[id]
        
        except IndexError:
            response = {
                'status': 'error',
                'message': f'id {id} data does not exist'
            }
    
    elif request.method == 'PUT':
        response = json.loads(request.data)
        TASKS[id] = response

        message = {'message': f'id {id} updated with successfully'}
        return jsonify(message)

    elif request.method == 'DELETE':
        TASKS.pop(id)

        message = {
            'message': f'id {id} deleted with successfully'
        }

        return jsonify(message)
        
    return jsonify(response)


if __name__ == '__main__':
    app.run(debug=True)