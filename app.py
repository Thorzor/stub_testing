from flask import Flask

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


if __name__ == '__main__':
    app.run()
