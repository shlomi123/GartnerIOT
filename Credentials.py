"""Application Config"""
import os


MQTT_HOST = os.environ.get("mqtt-host", 'm10.cloudmqtt.com')
MQTT_USER = os.environ.get("mqtt-user", 'dmyknjpx')
MQTT_PWD = os.environ.get("mqtt-pwd", 'MVchQL66o8ZH')
MQTT_PORT = int(os.environ.get("mqtt-port", 14571))
MQTT_FB_WEBHOOK_TOPIC_NAME = 'fb-posts-updates'
WEB_PORT = int(os.environ.get("PORT", 5000))
