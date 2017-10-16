from gateway import Server
import Credentials
from mqtt import MqttClient
from MSg import Msg

# pylint: disable=invalid-name
server = Server()

if __name__ == '__main__':
    server.app.run(host='0.0.0.0', port=Credentials.WEB_PORT)
