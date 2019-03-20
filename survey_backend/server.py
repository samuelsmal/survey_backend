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

    user_file_path = f"{__DATABASE__}/additional_data/{request.json['user_id']}.json"
    user_file = pathlib.Path(user_file_path)
    user_file.parent.mkdir(parents=True, exist_ok=True)

    print(f"submitUserData getting {request.json}\n\n")

    if user_file.is_file():
        with open(user_file, 'r') as f:
            user_data = json.load(f)
            user_data['data'] += [request.json]
    else:
        user_data = {'user_id': request.json['user_id'], 'data': [request.json]}

    with open(user_file, 'w') as f:
        json.dump(user_data, f)

    return Response(status=200)


@app.route('/submitAnswers', methods=['POST'])
def submitAnswers():
    if not request.json or 'user_id' not in request.json:
        abort(400)

    file_path = f"{__DATABASE__}/answers/{request.json['user_id']}.json"
    file = pathlib.Path(file_path)
    file.parent.mkdir(parents=True, exist_ok=True)

    if file.is_file():
        with open(file, 'r') as f:
            try:
                old_answers = json.load(f)
                if old_answers == '':
                    old_answers = []
            except JSONDecodeError as e:
                old_answers = []
    else:
        old_answers = []

    with open(file, 'w') as f:
        f.write(json.dumps(old_answers + [request.json['answers']]))

    return Response(status=200)

@app.route('/test', methods=['GET'])
def test():
    return 'yep'

if __name__ == '__main__':
    app.run(host='localhost', port=5000)
