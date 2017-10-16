import json
import paho.mqtt.client as paho
import Credentials


class MqttClient:
    """A facade api to  MQTT client"""

    def __init__(self):
        self.mqttc = paho.Client()
        self.mqttc.username_pw_set(Credentials.MQTT_USER, Credentials.MQTT_PWD)

        try:
            self.mqttc.connect(Credentials.MQTT_HOST, Credentials.MQTT_PORT)
        except ValueError:
            print "oooooopppps"

    def publish(self, topic, message):
        """Publishes a new message to a topic"""
        return self.mqttc.publish(topic, json.dumps(message.__dict__))
