import json
import random
import time
import asyncio

from flask import Flask, request, jsonify

from methods import stub_response, stub_update, payout, payout_update, payout_status, status_payout_update

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
    if "1111111111" in str(body["request"]["account"]):
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
    elif "2222222222" in str(body["request"]["account"]):
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
    elif "3333333333" in str(body["request"]["account"]):
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
    elif "4444444444" in str(body["request"]["account"]):
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
    elif "5555555555" in str(body["request"]["account"]):
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


@app.route('/pay/direct/update', methods=['PUT'])
def update_payout():
    return stub_update.stub_update()


@app.route('/v1/payout/status/update', methods=['PUT'])
def update_payout_status():
    return status_payout_update.stub_update()


@app.route('/pay/direct', methods=['POST'])
def stub_process():
    return stub_response.stub_resp()


@app.route('/v1/payout', methods=['POST'])
def process_payout():
    return payout.stub_resp()


@app.route('/cards/<card_id>', methods=['GET'])
def process_cards_id(card_id):
    canceled_status = {
        "encryptedPaymentData": {
            "paymentToken": {
                "paymentAccountReference": "5001EUMYTT3AESCZGUEC77KPCLETI",
                "paymentToken": "5972374364093457",
                "tokenExpirationMonth": "05",
                "tokenExpirationYear": "2022"
            }
        },
        "maskedCard": {
            "dateOfCardCreated": "2021-11-25T14:51:03.811Z",
            "delegatedAuthenticationModels": [
                {
                    "isSupported": True,
                    "modelType": "AE_TYPE_3"
                }
            ],
            "digitalCardData": {
                "artUri": "https://assets.mastercard.com/card-art/combined-image-asset/MyBank-mastercard.png",
                "coBrandedName": "My Bank",
                "descriptorName": "Bank Rewards MasterCard",
                "isCoBranded": True,
                "pendingEvents": [
                    "PENDING_SCA"
                ],
                "status": "CANCELLED",
                "issuerName": "Issuing Bank",
                "longDescription": "Bank Rewards MasterCard with the super duper rewards program",
                "foregroundColor": "FF5733"
            },
            "panBin": "520473",
            "panExpirationMonth": "05",
            "panExpirationYear": "2022",
            "panLastFour": "4601",
            "paymentAccountReference": "5001EUMYTT3AESCZGUEC77KPCLETI",
            "paymentCardDescriptor": "mastercard",
            "paymentCardType": "CREDIT",
            "serviceId": "#serviceId_providedbyMastercard",
            "srcDigitalCardId": card_id,
            "tokenLastFour": "7217",
            "tokenUniqueReference": "DM4MMC0000000001cd2826c715b7475bb089b7622366ebe4",
            "tokenExpirationMonth": 10,
            "tokenExpirationYear": "2022"
        },
        "maskedConsumer": {
            "dateConsumerAdded": "2021-11-25T14:51:03.811Z",
            "maskedConsumerIdentity": {
                "identityType": "EXTERNAL_ACCOUNT_ID",
                "maskedIdentityValue": "90032****"
            }
        },
        "srcCorrelationId": "779165e0-1905-4edd-89fa-be46497b5044",
        "keyFingerprintId": "nwzNuN9upxolVsr6q0I/phcnfA/ZlaJ2gmAJiogMCwM"
    }
    suspended_status = {
        "encryptedPaymentData": {
            "paymentToken": {
                "paymentAccountReference": "5001EUMYTT3AESCZGUEC77KPCLETI",
                "paymentToken": "5972374364093457",
                "tokenExpirationMonth": "05",
                "tokenExpirationYear": "2022"
            }
        },
        "maskedCard": {
            "dateOfCardCreated": "2021-11-25T14:51:03.811Z",
            "delegatedAuthenticationModels": [
                {
                    "isSupported": True,
                    "modelType": "AE_TYPE_3"
                }
            ],
            "digitalCardData": {
                "artUri": "https://assets.mastercard.com/card-art/combined-image-asset/MyBank-mastercard.png",
                "coBrandedName": "My Bank",
                "descriptorName": "Bank Rewards MasterCard",
                "isCoBranded": True,
                "pendingEvents": [
                    "PENDING_SCA"
                ],
                "status": "SUSPENDED",
                "issuerName": "Issuing Bank",
                "longDescription": "Bank Rewards MasterCard with the super duper rewards program",
                "foregroundColor": "FF5733"
            },
            "panBin": "520473",
            "panExpirationMonth": "05",
            "panExpirationYear": "2022",
            "panLastFour": "4601",
            "paymentAccountReference": "5001EUMYTT3AESCZGUEC77KPCLETI",
            "paymentCardDescriptor": "mastercard",
            "paymentCardType": "CREDIT",
            "serviceId": "#serviceId_providedbyMastercard",
            "srcDigitalCardId": card_id,
            "tokenLastFour": "7217",
            "tokenUniqueReference": "DM4MMC0000000001cd2826c715b7475bb089b7622366ebe4",
            "tokenExpirationMonth": 10,
            "tokenExpirationYear": "2022"
        },
        "maskedConsumer": {
            "dateConsumerAdded": "2021-11-25T14:51:03.811Z",
            "maskedConsumerIdentity": {
                "identityType": "EXTERNAL_ACCOUNT_ID",
                "maskedIdentityValue": "90032****"
            }
        },
        "srcCorrelationId": "779165e0-1905-4edd-89fa-be46497b5044",
        "keyFingerprintId": "nwzNuN9upxolVsr6q0I/phcnfA/ZlaJ2gmAJiogMCwM"
    }
    if card_id == 'd4bce4b5-9d2b-493b-bb38-938784c37fc1':
        return jsonify(canceled_status), 200
    elif card_id == '8970c61e-36d4-4366-92b6-9833cf4c1e47':
        return jsonify(suspended_status), 200
    elif card_id == 'd89196a1-37e3-498b-aace-e8d971f6516b':
        return jsonify({'message': 'Case with 500 status code'}), 500


@app.route('/vts/merchant-api-ic/onboarding', methods=['POST'])
def process_vts():
    body = request.json()
    if body['primaryWebsiteURL'] == 'https://www.stub-service.online/':
        return jsonify({'message': 'Case with 500 status code'}), 500
    else:
        return jsonify({'message': 'Case with 400 status code'}), 400


@app.route('/verify', methods=['POST'])
def process_verify():
    body = request.get_json()
    if body['amount'] > 100:
        return jsonify({
            "code": 0,
            "uid": body['uid'],
            "amount": body['amount'],
            "created_at": body['created_at']
        }), 200
    elif body['amount'] < 100:
        return jsonify({
            "code": 1,
            "uid": body['uid'],
            "amount": body['amount'],
            "created_at": body['created_at']
        }), 200
    elif body['amount'] == 555:
        return jsonify({
            "uid": body['uid'],
            "amount": body['amount'],
            "created_at": body['created_at']
        }), 200
    elif body['amount'] == 111:
        return jsonify({
            "message": "Case with 500"
        }), 200
    elif body['amount'] == 222:
        return jsonify({
            "code": 0,
            "uid": body['uid'],
            "amount": body['amount'],
            "created_at": body['created_at']
        }),
    elif body['amount'] == 333:
        return jsonify({
            "message": "Case with 400"
        }), 400
    elif body['amount'] == 123:
        time.sleep(11)
        return jsonify({
            "code": 0,
            "uid": body['uid'],
            "amount": body['amount'],
            "created_at": body['created_at']
        }), 400


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
