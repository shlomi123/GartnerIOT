class Msg(object):
    """ A Msg to send upon action"""

    def __init__(self, time, msgType, user_id):
        self.time = time
        self.type = msgType
        self.user_id = user_id