from flask import *
from flask_api import *
from flask import request
from flask import jsonify

app = FlaskAPI(__name__)


JSON = [{
 "name": "John",
 "age": 30,
 "cars": ["Ford", "BMW", "Fiat"]
}]


@app.route("/", methods=['GET'])
def send_json():
    return jsonify({'json': JSON})


@app.route("/", methods=['POST'])
def save_json():
    content = request.get_json()
    JSON.append(content)

if __name__ == "__main__":
    app.run(debug=True)
