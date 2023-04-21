from flask import json

def stub_resp():
    with open('stub/stub_response.json', 'r') as json_file:
        file_data = json.load(json_file)
        json_file.close()
        return file_data