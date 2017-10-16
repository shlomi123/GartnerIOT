from flask import *
from mqtt import MqttClient
import Credentials
from MSg import Msg


class Server(object):
    """Server class"""
    app = Flask(__name__)
    MQTTC = MqttClient()

    @app.route("/")
    def hello(self):
        """default"""
        return "Hello World!"

    @app.route("/webhook", methods=['GET'])
    def verify(self):
        """webhook api"""
        return request.args.get('hub.challenge')

    @app.route("/webhook", methods=['POST'])
    def fb_feeds_webhook(self):
        """webhook api"""
        content = request.get_json()
        if content['entry'][0]['changes'][0]['value']['item'] == 'like':
            Server.MQTTC.publish(Credentials.MQTT_FB_WEBHOOK_TOPIC_NAME, Msg(int(content['entry'][0]['time']),
            'LIKE', content['entry'][0]['changes'][0]['value']['user_id']))


