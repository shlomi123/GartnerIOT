from flask import *
from flask import request
from flask import jsonify
import os
from paho import mqtt

app = Flask(__name__)


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

app.run(host='0.0.0.0', port=os.environ.get("PORT", 5000))
