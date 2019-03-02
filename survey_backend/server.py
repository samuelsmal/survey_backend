import pathlib
import json
import logging
from flask import Flask, request, abort, Response
from flask_cors import CORS

__DATABASE__ = './raw_data/'
app = Flask(__name__)
CORS(app)

@app.route('/submitAnswers', methods=['POST'])
def submitAnswers():
    if not request.json or 'user_id' not in request.json:
        abort(400)
    #print(request.json)

    pathlib.Path(__DATABASE__).mkdir(parents=True, exist_ok=True)
    with open(__DATABASE__ + str(request.json['user_id']) + '.json', 'w') as f:
        json.dump(request.json['answers'], f)

    return Response(status=200)

@app.route('/test', methods=['GET'])
def test():
    return 'yep'

if __name__ == '__main__':
    app.run(host='localhost', port=5000)
