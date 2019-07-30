from utils.strips import NervesServer

# IP for the socket server
SERVER_IP = '192.168.1.136'

# Port for the socket server
SERVER_PORT = 2052

# Select the correct server type
SERVER_TYPE = NervesServer

# It's possible to simulate multiple short strips within single longer one
STRIPS = [
    {
        'name': 'room',
        'start': 0,
        'end': 0
    },
]
