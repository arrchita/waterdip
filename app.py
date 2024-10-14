from flask import Flask, request, jsonify

app = Flask(__name__)

tasks = []

@app.route('/v1/tasks', methods=['POST'])
def create_task():
    data = request.get_json()
    task_id = len(tasks) + 1
    task = {'id': task_id, 'title': data['title'], 'is_completed': False}
    tasks.append(task)
    return jsonify({'id': task_id}), 201


@app.route('/v1/tasks', methods=['GET'])
def list_tasks():
    return jsonify({'tasks': tasks}), 200


@app.route('/v1/tasks/<int:id>', methods=['GET'])
def get_task(id):
    task = next((t for t in tasks if t['id'] == id), None)
    if task is None:
        return jsonify({'error': 'There is no task at that id'}), 404
    return jsonify(task), 200


@app.route('/v1/tasks/<int:id>', methods=['PUT'])
def update_task(id):
    task = next((t for t in tasks if t['id'] == id), None)
    if task is None:
        return jsonify({'error': 'There is no task at that id'}), 404
    data = request.get_json()
    task['title'] = data.get('title', task['title'])
    task['is_completed'] = data.get('is_completed', task['is_completed'])
    return '', 204


@app.route('/v1/tasks/<int:id>', methods=['DELETE'])
def delete_task(id):
    global tasks
    tasks = [t for t in tasks if t['id'] != id]
    return '', 204


if __name__ == '__main__':
    app.run(debug=True)
