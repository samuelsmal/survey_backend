import logging
from flask import Flask, request, abort, Response
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/submitAnswers', methods=['POST'])
def submitAnswers():
    if not request.json:
        abort(400)
    print(request.json)
    return Response(status=200)

@app.route('/test', methods=['GET'])
def test():
    return 'yep'

if __name__ == '__main__':
    app.run(host='localhost', port=5000)
