import json
import random
import time
import asyncio

from flask import Flask, request, jsonify

from methods import stub_response, stub_update
from methods.count import Counter

app = Flask(__name__)
loop = asyncio.get_event_loop()
counter_object_1 = Counter()
counter_object_2 = Counter()
counter_object_3 = Counter()


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
    elif body["request"]["account"] == 'newtankistwot_400@gmail.com':
        return jsonify({'message': 'Case with 422 status code'}), 422
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


@app.route('/stub/erip/account_verification', methods=['POST'])
def erip_account_verification():
    body = request.get_json()
    if not request.data:
        return jsonify({'message': 'Body is empty'}), 400
    if body["request"]["account"] == "1111111111":
        return jsonify({
            "response": {
                "bg_uuid": "3542-24t24g2424242-234t22-235vertyui",
                "tracking_id": "your_uniq_number",
                "amount": 100,
                "editable_amount": True,
                "currency": "RUB",
                "result": "0",
                "description": "0"
            }
        }), 200
    elif body["request"]["account"] == "2222222222":
        return jsonify({
            "response": {
                "bg_uuid": "3542-24t24g2424242-234t22-235vertyui",
                "tracking_id": "your_uniq_number",
                "amount": 100,
                "editable_amount": True,
                "currency": "RUB",
                "result": "0",
                "description": "0",
                "person": {
                    "first_name": "client_name",
                    "last_name": "client_surname",
                    "middle_name": "client_patronymic",
                },
                "hint": [
                    {
                        "hintline": "message_1",
                    },
                    {
                        "hintline": "message_1",
                    },
                    {
                        "hintline": "message_n"
                    },
                ]
            }
        }), 200
    elif body["request"]["account"] == "3333333333":
        time.sleep(15)
        return jsonify({
            "response": {
                "bg_uuid": "3542-24t24g2424242-234t22-235vertyui",
                "tracking_id": "your_uniq_number",
                "amount": 100,
                "editable_amount": True,
                "currency": "RUB",
                "result": "0",
                "description": "0",
                "person": {
                    "first_name": "client_name",
                    "last_name": "client_surname",
                    "middle_name": "client_patronymic",
                },
                "hint": [
                    {
                        "hintline": "message_1",
                    },
                    {
                        "hintline": "message_1",
                    },
                    {
                        "hintline": "message_n"
                    },
                ]
            }
        }), 200
    elif body["request"]["account"] == "4444444444":
        return jsonify({
            "response": {
                "bg_uuid": "3542-24t24g2424242-234t22-235vertyui",
                "tracking_id": "your_uniq_number",
                "amount": 0,
                "editable_amount": True,
                "currency": "RUB",
                "result": "3",
                "description": "0",
                "person": {
                    "first_name": "client_name",
                    "last_name": "client_surname",
                    "middle_name": "client_patronymic",
                },
                "hint": [
                    {
                        "hintline": "message_1",
                    },
                    {
                        "hintline": "message_1",
                    },
                    {
                        "hintline": "message_n"
                    },
                ]
            }
        })
    elif body["request"]["account"] == "5555555555":
        return jsonify({
            "response": {
                "bg_uuid": "3542-24t24g2424242-234t22-235vertyui",
                "tracking_id": "your_uniq_number",
                "amount": 100,
                "editable_amount": True,
                "currency": "RUB",
                "description": "0",
                "person": {
                    "first_name": "client_name",
                    "last_name": "client_surname",
                    "middle_name": "client_patronymic",
                },
                "hint": [
                    {
                        "hintline": "message_1",
                    },
                    {
                        "hintline": "message_1",
                    },
                    {
                        "hintline": "message_n"
                    },
                ]
            }
        })


@app.route('/stub/erip_callback', methods=['POST'])
def process_erip_callback():
    body = request.get_json()
    if body['transaction']['qiwi_terminal']['account_number'] == '7777777777':
        return jsonify({'message': 'Case with 500 status code'}), 500
    elif body['transaction']['qiwi_terminal']['account_number'] == '8888888888':
        return jsonify({'message': 'Successful callback'}), 200


@app.route('/get_counter', methods=['GET'])
def get_counter():
    return jsonify({'counter': f'{counter_object_1.get_counter_value()}'}), 200


@app.route('/v1/payout/status', methods=['POST'])
def stub_process():
    body = request.get_json()

    if not request.data:
        return jsonify({'message': 'Body is empty'}), 400
    order_id = body['order_id']

    if body['card_exp_year'] == '27':
        if counter_object_1.get_counter_value() == 3:
            counter_object_1.reset_counter()
            return jsonify({
                "payment_status": "fail", "id": 100000536, "order_id": f"{order_id}", "amount": "300.00",
                "payment_amount": "300.00", "is_partial_payment": False, "account_payment_amount": 290,
                "commission_amount": 10, "service_code": "payment_card_rub", "account_old_balance": 1290,
                "account_new_balance": 1000}), 200
        else:
            counter_object_1.update_counter()
            return jsonify({
                "payment_status": "wait", "id": 100000536, "order_id": f"{order_id}", "amount": "300.00",
                "payment_amount": "300.00", "is_partial_payment": False, "account_payment_amount": 290,
                "commission_amount": 10, "service_code": "payment_card_rub", "account_old_balance": 1290,
                "account_new_balance": 1000}), 200

    elif body['card_exp_year'] == '29':
        if counter_object_1.get_counter_value() == 4:
            counter_object_2.reset_counter()
            return jsonify({
                "payment_status": "cancel", "id": 100000536, "order_id": f"{order_id}", "amount": "300.00",
                "payment_amount": "300.00", "is_partial_payment": False, "account_payment_amount": 290,
                "commission_amount": 10, "service_code": "payment_card_rub", "account_old_balance": 1290,
                "account_new_balance": 1000}), 200
        else:
            counter_object_2.update_counter()
            return jsonify({
                "payment_status": "wait", "id": 100000536, "order_id": f"{order_id}", "amount": "300.00",
                "payment_amount": "300.00", "is_partial_payment": False, "account_payment_amount": 290,
                "commission_amount": 10, "service_code": "payment_card_rub", "account_old_balance": 1290,
                "account_new_balance": 1000}), 200

    elif body['card_exp_year'] == '30':
        if counter_object_3.get_counter_value() == 5:
            counter_object_3.reset_counter()
            return jsonify({
                "payment_status": "paid", "id": 100000536, "order_id": f"{order_id}", "amount": "300.00",
                "payment_amount": "300.00", "is_partial_payment": False, "account_payment_amount": 290,
                "commission_amount": 10, "service_code": "payment_card_rub", "account_old_balance": 1290,
                "account_new_balance": 1000}), 200
        else:
            counter_object_3.update_counter()
            return jsonify({
                "payment_status": "wait", "id": 100000536, "order_id": f"{order_id}", "amount": "300.00",
                "payment_amount": "300.00", "is_partial_payment": False, "account_payment_amount": 290,
                "commission_amount": 10, "service_code": "payment_card_rub", "account_old_balance": 1290,
                "account_new_balance": 1000}), 200

    elif body['card_exp_year'] == '31':
        return jsonify({'message': 'Case with 500 status code'}), 500


    else:
        return jsonify({
            "payment_status": "wait", "id": 100000536, "order_id": f"{order_id}", "amount": "300.00",
            "payment_amount": "300.00", "is_partial_payment": False, "account_payment_amount": 290,
            "commission_amount": 10, "service_code": "payment_card_rub", "account_old_balance": 1290,
            "account_new_balance": 1000}), 200


@app.route('/v1/payout', methods=['POST'])
def process_payout():
    return jsonify({"payment_status": "wait", "id": random.randint(100000000, 999999999)}), 200


if __name__ == '__main__':
    loop.run_until_complete(asyncio.sleep(0))
    app.run(host='0.0.0.0', port=5000)
