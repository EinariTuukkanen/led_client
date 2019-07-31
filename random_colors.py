#!/usr/bin/python3
import time
import socket

from utils.colors import random_rgbs, random_rgbws
from core import strips, connect_all

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
connect_all(sock)

room = strips['room']

colors = random_rgbws(room.length)
# colors = [[0, 0, 255, 0]] * room.length
room.set_colors(colors)
