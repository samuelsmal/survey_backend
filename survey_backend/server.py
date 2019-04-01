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

def _is_user_id_ok_(user_id):
    with open(f'{__DATABASE__}/user_assigments.json', 'r') as f:
        return str(user_id) in json.load(f)


@app.route('/getQuestions/<api_token>/<participant_id>/<language>', methods=['GET'])
def getQuestions(api_token, participant_id, language):
    if not _is_user_id_ok_(participant_id):
        abort(400)

    try:
        with open(__DATABASE__ + '/user_assigments.json', 'r') as f:
            user_assigments = json.load(f)[str(participant_id)]
    except KeyError as e:
        print("error with getting questions {participant_id} {language}")

        abort(400)

    questions = []

    for ct_choice, dt_choice in zip(user_assigments['ct_questions'], user_assigments['dt_questions']):
        with open(f'{__DATABASE__}/ct_{language}_{ct_choice:0>2}.json', 'r') as f:
            questions += [json.load(f)]


        with open(f'{__DATABASE__}/dt_{language}.json', 'r') as f:
            questions += [[q for i, q in enumerate(json.load(f)) if i in [dt_choice]]]

    return jsonify({'questions': questions,
                    'music_order': user_assigments['music_order']})


@app.route('/submitUserData/<api_token>', methods=['POST'])
def submitUserData(api_token):
    if not request.json or 'user_id' not in request.json or not _is_user_id_ok_(request.json['user_id']):
        abort(400)

    user_file_path = f"{__DATABASE__}/additional_data/{request.json['user_id']}.json"
    user_file = pathlib.Path(user_file_path)
    user_file.parent.mkdir(parents=True, exist_ok=True)

    #print(f"submitUserData getting {request.json}\n\n")

    payload = [{'api_token': api_token, 'data': request.json}]

    if user_file.is_file():
        with open(user_file, 'r') as f:
            user_data = json.load(f)
            user_data += payload
    else:
        user_data = payload

    with open(user_file, 'w') as f:
        json.dump(user_data, f)

    return Response(status=200)


@app.route('/submitAnswers/<api_token>', methods=['POST'])
def submitAnswers(api_token):
    if not request.json or 'user_id' not in request.json or not _is_user_id_ok_(request.json['user_id']):
        abort(400)

    file_path = f"{__DATABASE__}/answers/{request.json['user_id']}.json"
    file = pathlib.Path(file_path)
    file.parent.mkdir(parents=True, exist_ok=True)

    payload = [{'api_token': api_token, 'data': request.json['answers']}]

    if file.is_file():
        with open(file, 'r') as f:
            answers = json.load(f)
            answers += payload
    else:
        answers = payload

    with open(file, 'w') as f:
        json.dump(answers, f)

    return Response(status=200)

@app.route('/test', methods=['GET'])
def test():
    return 'yep'

if __name__ == '__main__':
    app.run(host='localhost', port=5000)
