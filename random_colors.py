#!/usr/bin/python3
import socket

from utils.colors import random_rgbs
from core import strips, connect_all

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
connect_all(sock)

room = strips['room']
colors = random_rgbs(100)

room.set_colors(colors)
