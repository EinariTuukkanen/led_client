import utils.packet_pb2 as pb


class BaseStrip:
    def __init__(self, name, start, end):
        self.name = name
        self.start = start
        self.end = end
        self.length = end - start

    def connect(self, sock, ip, port):
        self.sock = sock
        self.ip = ip
        self.port = port


class NervesStrip(BaseStrip):
    def set_colors(self, colors, offset=0):
        packet = pb.Packet()
        packet.offset = offset
        for rgb in colors:
            for color in rgb:
                packet.colors += bytes([color])

        self.sock.sendto(
            packet.SerializeToString(),
            (self.ip, self.port))


NervesServer = NervesStrip
