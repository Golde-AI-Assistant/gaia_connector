from flask import request, jsonify
import requests

from controllers import app
from controllers.controller_config.config import ControllerConfig


task_manager_url = ControllerConfig('task_manager').url

@app.route('/create-task', methods=['POST'])
def create_task():
    data = request.get_json()
    task = data['task']
    
    task_response = requests.post(f"{task_manager_url}/create-task", json={'task': task})
    
    if task_response.status_code == 200:
        return jsonify({'response': task_response.json()})
    else :
        return jsonify({'response': 'Cannot create task'})
    
@app.route('/update-task', methods=['PUT'])
def update_task():
    data = request.get_json()
    task = data['task']
    
    task_response = requests.put(f"{task_manager_url}/update-task", json={'task': task})
    
    if task_response.status_code == 200:
        return jsonify({'response': task_response.json()})
    else :
        return jsonify({'response': 'Cannot update task'})
    
@app.route('/delete-task', methods=['DELETE'])
def delete_task():
    data = request.get_json()
    task = data['task']
    
    task_response = requests.delete(f"{task_manager_url}/delete-task", json={'task': task})
    
    if task_response.status_code == 200:
        return jsonify({'response': task_response.json()})
    else :
        return jsonify({'response': 'Cannot delete task'})  
    
@app.route('/view-task', methods=['GET'])
def view_task():
    data = request.get_json()
    task = data['task']
    
    task_response = requests.get(f"{task_manager_url}/view-task", json={'task': task})
    
    if task_response.status_code == 200:
        return jsonify({'response': task_response.json()})
    else :
        return jsonify({'response': 'Cannot view task'})