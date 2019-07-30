#!/usr/bin/python3
import socket

from core import strips, connect_all

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
connect_all(sock)

room = strips['room']
colors = [[0, 0, 0]] * 100

room.set_colors(colors)
