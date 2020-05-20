from logging import getLogger, Formatter, StreamHandler, DEBUG


def get_logger():
    logger = getLogger(__name__)
    handler = StreamHandler()
    fmr = Formatter("[%(levelname)s] %(lineno)d %(asctime)s %(funcName)s >>\t%(message)s")
    handler.setFormatter(fmr)
    handler.setLevel(DEBUG)
    logger.setLevel(DEBUG)
    logger.addHandler(handler)

    return logger
