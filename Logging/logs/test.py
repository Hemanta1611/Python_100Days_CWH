import logger
import logging

def add(a, b):
    logging.debug(f"Adding {a} + {b}")
    return a + b


logging.debug("The addition function is called")
add(1, 2)