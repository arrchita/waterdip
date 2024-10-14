from flask import Blueprint, request, jsonify
from models import db, Task

task_bp = Blueprint('task', __name__)

@task_bp.route('/v1/tasks', methods=['POST'])
def create_task():
    data = request.get_json()
    new_task = Task(title=data['title'])
    db.session.add(new_task)
    db.session.commit()
    return jsonify({'id': new_task.id}), 201

@task_bp.route('/v1/tasks', methods=['GET'])
def list_tasks():
    tasks = Task.query.all()
    tasks_list = [{'id': task.id, 'title': task.title, 'is_completed': task.is_completed} for task in tasks]
    return jsonify({'tasks': tasks_list}), 200

@task_bp.route('/v1/tasks/<int:id>', methods=['GET'])
def get_task(id):
    task = Task.query.get_or_404(id)
    return jsonify({'id': task.id, 'title': task.title, 'is_completed': task.is_completed}), 200

@task_bp.route('/v1/tasks/<int:id>', methods=['PUT'])
def update_task(id):
    task = Task.query.get_or_404(id)
    data = request.get_json()
    task.title = data.get('title', task.title)
    task.is_completed = data.get('is_completed', task.is_completed)
    db.session.commit()
    return '', 204

@task_bp.route('/v1/tasks/<int:id>', methods=['DELETE'])
def delete_task(id):
    task = Task.query.get_or_404(id)
    db.session.delete(task)
    db.session.commit()
    return '', 204
