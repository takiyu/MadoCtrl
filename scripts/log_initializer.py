# -*- coding: utf-8 -*-
import logging

datefmt = '%Y/%m/%d %H:%M:%S'

# default log format
default_fmt = logging.Formatter('[%(asctime)s.%(msecs)d] %(levelname)s '
                                '(%(process)d) %(name)s : %(message)s',
                                datefmt=datefmt)

# set up handler
try:
    # Rainbow Logging
    import sys
    from rainbow_logging_handler import RainbowLoggingHandler
    default_handler = RainbowLoggingHandler(sys.stdout,
                                            color_msecs=('black', None, True),
                                            datefmt=datefmt)
except Exception:
    default_handler = logging.StreamHandler()

default_handler.setFormatter(default_fmt)
default_handler.setLevel(logging.DEBUG)

# setup root logger
logger = logging.getLogger()
logger.addHandler(default_handler)
logger.setLevel(logging.DEBUG)


def set_fmt(fmt=default_fmt):
    global defaut_handler
    default_handler.setFormatter(fmt)


def set_root_level(level):
    global logger
    logger.setLevel(level)
