from itertools import product
import pathlib
import json
from json import JSONDecodeError
import logging
from flask import Flask, request, abort, Response, jsonify
from flask_cors import CORS

__DATABASE__ = __file__[:-len(__name__ + '.py')] + 'data/'
app = Flask(__name__)
CORS(app)

@app.route('/getQuestions/<participant_id>/<language>', methods=['GET'])
def getQuestions(participant_id, language):
    # TODO do the selection
    # returns a json array of the questions in the order for this participant
    questions = {}
    for question_type, language in product(['dt'], ['fr']):
        with open(f'{__DATABASE__}/{question_type}_{language}.json', 'r') as f:
            questions[question_type] = json.load(f)

    return jsonify(list(questions.values()))


@app.route('/submitUserData', methods=['POST'])
def submitUserData():
    if not request.json or 'user_id' not in request.json:
        abort(400)

    user_file = __DATABASE__ + '/additional_data/' + str(request.json['user_id']) + '.json'
    pathlib.Path(user_file).parent.mkdir(parents=True, exist_ok=True)

    with open(user_file, 'w') as f:
        json.dump(request.json, f)

    return Response(status=200)


@app.route('/submitAnswers', methods=['POST'])
def submitAnswers():
    if not request.json or 'user_id' not in request.json:
        abort(400)
    #print(request.json)

    user_file = __DATABASE__ + '/answers/' + str(request.json['user_id']) + '.json'
    pathlib.Path(user_file).parent.mkdir(parents=True, exist_ok=True)

    if pathlib.Path(user_file).is_file():
        with open(user_file, 'r') as f:
            try:
                old_answers = json.load(f)
                if old_answers == '':
                    old_answers = []
            except JSONDecodeError as e:
                old_answers = []
    else:
        old_answers = []

    with open(user_file, 'w') as f:
        f.write(json.dumps(old_answers + [request.json['answers']]))

    return Response(status=200)

@app.route('/test', methods=['GET'])
def test():
    return 'yep'

if __name__ == '__main__':
    app.run(host='localhost', port=5000)
