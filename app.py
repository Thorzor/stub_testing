import json
import time

from flask import Flask, request, jsonify

from methods import stub_response, stub_update

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Это крутой микросервис который много чего может'


# Отдает содержимое файла stub_response.json
@app.route('/get_stub', methods=['POST'])
def get_stub_response():
    return stub_response.stub_resp()


# Обновляет содержимое файла stub_response.json
@app.route('/stub_update', methods=['PUT'])
def stub_put():
    return stub_update.stub_update()


@app.route('/stub/account_verification', methods=['POST'])
def account_verification():
    body = request.get_json()
    if not request.data:
        return jsonify({'message': 'Body is empty'}), 400
    if body["request"]["account"] == 'newtankistwot@gmail.com':
        return jsonify({'response': {'result': '0'}}), 200
    elif body["request"]["account"] == 'newtankistwot_1@gmail.com':
        return jsonify({'response': {'result': '1'}}), 200
    elif body["request"]["account"] == 'newtankistwot_4@gmail.com':
        return jsonify({'response': {'result': '4'}}), 200
    elif body["request"]["account"] == 'newtankistwot_5@gmail.com':
        return jsonify({'response': {'result': '5'}}), 200
    elif body["request"]["account"] == 'newtankistwot_7@gmail.com':
        return jsonify({'response': {'result': '7'}}), 200
    elif body["request"]["account"] == 'newtankistwot_8@gmail.com':
        return jsonify({'response': {'result': '8'}}), 200
    elif body["request"]["account"] == 'newtankistwot_500@gmail.com':
        return jsonify({'message': 'Case with 500 status code'}), 500
    elif body["request"]["account"] == 'newtankistwot_15@gmail.com':
        time.sleep(15)
    elif body["request"]["account"] == 'newtankistwot_10@gmail.com':
        return jsonify({'response': {'result': '0'}}), 200
    elif body["request"]["account"] == 'newtankistwot_11@gmail.com':
        return jsonify({'response': {'result': '0'}}), 200
    elif body["request"]["account"] == 'newtankistwot_13@gmail.com':
        return jsonify({'response': {'result': '13'}}), 200


@app.route('/stub/callback', methods=['POST'])
def process_callback():
    body = request.get_json()
    if body['transaction']['qiwi_terminal']['account_number'] == 'newtankistwot_10@gmail.com':
        return jsonify({'message': 'Case with 500 status code'}), 500
    elif body['transaction']['qiwi_terminal']['account_number'] == 'newtankistwot_11@gmail.com':
        return jsonify({'message': 'Case with 400 status code'}), 400
    else:
        return jsonify({'message': 'Successful callback'}), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
