from flask import Flask, abort, jsonify, request

app = Flask(__name__)
tasks = []


@app.route('/add_user_info', methods=['post'])
def add_user_info():
    if not request.json or 'id' not in request.json or 'info' not in request.json:
        abort(400)
    task = {
        'id': request.json['id'],
        'info': request.json['info']
    }
    tasks.append(task)
    return jsonify({'code': 200, 'msg': 'success'})


@app.route('/get_task', methods=['get'])
def get_task():
    if not request.args or 'id' not in request.args:
        return jsonify(tasks)
    else:
        task_id = request.args['id']
        task = filter(lambda t: t['id'] == int(task_id), tasks)
        return jsonify(task) if task else jsonify({'result': 'Not found'})


if __name__ == '__main__':
    app.run(port=5000, debug=True, host='127.0.0.1')
