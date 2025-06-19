import logging

# logging settings
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[
        logging.FileHandler("app1.log"),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger("Arithmetic App")

def add(a, b):
    logger.debug(f"Adding {a} + {b}: {a+b}")
    return a + b

def subtract(a, b):
    logger.debug(f"Subtracting {a} - {b}: {a-b}")
    return a - b

def multiply(a, b):
    logger.debug(f"Multiplying {a} * {b}: {a*b}")
    return a * b

def divide(a, b):
    try:
        logger.debug(f"Dividing {a} / {b}: {a/b}")
        return a / b
    except ZeroDivisionError:
        logger.error("Cannot divide by zero")
        return None

    
add(2, 9)
subtract(9, 2)
multiply(2, 9)
divide(9, 2)