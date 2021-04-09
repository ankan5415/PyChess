import logging
from termcolor import colored

logging.basicConfig(format="%(levelname)s:%(message)s", level=logging.DEBUG)


def logInit(func):
    def logWrapper(*args, **kwargs):
        logging.debug(colored(func.__name__, "red"))
        func()

    return logWrapper