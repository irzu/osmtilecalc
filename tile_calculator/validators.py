import argparse


def valid_latitude(arg):
    """Validates latitude input"""
    value = int(arg)
    if value > 90 or value < -90:
        msg = "%r is not a valid latitude" % arg
        raise argparse.ArgumentTypeError(msg)
    return value


def valid_longitude(arg):
    """Validates longitude input"""
    value = int(arg)
    if value > 180 or value < -180:
        msg = "%r is not a valid longitude" % arg
        raise argparse.ArgumentTypeError(msg)
    return value


def valid_zoomlevel(arg):
    """Validates zoom level input"""
    value = int(arg)
    if value > 21 or value < 0:
        msg = "%r is not a valid zoom level" % arg
        raise argparse.ArgumentTypeError(msg)
    return value
