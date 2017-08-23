import socket

nounix = False

try:
    socket.AF_UNIX
except:
    nounix = True

client = None


def init():
    global client

    if not nounix:
        client = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)
        client.connect('/tmp/autopylot_socket')


def update_robot(v, w):
    if w > 0.3: w = 0.3
    if w < -0.3: w = -0.3
    if v > 0.3: v = 0.3


    global client
    if not nounix:
        message = str(v) + ' ' + str(w)
        client.send(message.encode('utf8'))


def close():
    global client
    if not nounix:
        client.close()
