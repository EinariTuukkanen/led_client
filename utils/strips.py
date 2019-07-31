from threading import Thread
from time import sleep

import utils.packet_pb2 as pb
from utils.colors import rgb_to_hex


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

    def set_colors(self):
        raise Exception('Must be implemented by a subclass.')


class NervesStrip(BaseStrip):
    def set_colors(self, colors, offset=0):
        packet = pb.Packet()
        packet.offset = self.start
        for rgb in colors:
            for color in rgb:
                packet.colors += bytes([color])

        self.sock.sendto(
            packet.SerializeToString(),
            (self.ip, self.port))


class VirtualStrip(Thread):
    def __init__(self, name, start, end):
        # TODO: multi inherit from BaseStrip so duplicate code can be removed
        super().__init__()
        self.name = name
        self.start_index = start
        self.end_index = end
        self.length = end - start
        self.daemon = True
        self.start()

    def connect(self, *args, **kwargs):
        pass

    def run(self):
        # HACK: must be imported here to be able to run tkinter in thread
        import tkinter as tk

        # Configure
        width = 2000
        height = 20

        self.window = tk.Tk()
        self.canvas = tk.Canvas(self.window, bg='#fff',
                                width=width, height=height)

        pixel_size = width // self.length
        self.pixels = [
            self.canvas.create_rectangle(pixel_size * i, 0,
                                         pixel_size * (i + 1), pixel_size,
                                         outline="#000", fill="#fff")
            for i in range(0, self.length)
        ]
        self.canvas.pack()
        self.window.mainloop()

    def set_colors(self, colors, offset=0):
        # HACK: Waits for the run thread to start
        while not hasattr(self, 'pixels'):
            sleep(0.1)

        for i, pixel in enumerate(self.pixels[offset:]):
            self.canvas.itemconfig(pixel, fill=rgb_to_hex(*colors[i]))


NervesServer = NervesStrip
VirtualServer = VirtualStrip
