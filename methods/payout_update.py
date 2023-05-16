from flask import request, json


def stub_update():
    if request.method == "PUT":
        with open('stub/payout.json', 'w') as outfile:
            json.dump(request.json, outfile)
            outfile.close()

        with open('stub/payout.json', 'r') as json_file:
            file_data = json.load(json_file)
            json_file.close()

        return file_data
