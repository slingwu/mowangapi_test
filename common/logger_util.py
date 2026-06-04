import logging

def get_logger(name="mowang"):
    logger=logging.getLogger(name)
    if not logger.handlers:
        logger.setLevel(logging.INFO)
        handeler=logging.StreamHandler()
        formatter=logging.Formatter('%(asctime)s| %(levelname)s | %(message)s')
        handeler.setFormatter(formatter)
        logger.addHandler(handeler)
    return logger