from flask import Flask, json

server = Flask(__name__)


@server.route('/index', methods=['get', 'post'])
def index():
    res = {'msg': "python 接口", 'msg_code': 0}
    return json.dumps(res, ensure_ascii=False)


@server.route('/reg', methods=['post'])
def reg():
    res = {'msg': 'reg接口', 'msg_code': 200}
    return json.dumps(res, ensure_ascii=False)


if __name__ == "__main__":
    server.run(port=5000, debug=True, host="0.0.0.0")
