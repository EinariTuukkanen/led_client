import config as cfg


def connect_strip(name, sock, ip=cfg.SERVER_IP, port=cfg.SERVER_PORT):
    """ Connects strip to specified socket server """
    strips[name].connect(sock, ip, port)


def connect_all(sock, ip=cfg.SERVER_IP, port=cfg.SERVER_PORT):
    """ Shortcut for connecting all strips to same server """
    for name in strips:
        connect_strip(name, sock, ip, port)


# Build strip dict with names as keys and strips as values
strips = {
    s['name']: cfg.SERVER_TYPE(s['name'], s['start'], s['end'])
    for s in cfg.STRIPS
}
