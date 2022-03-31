from logging import DEBUG, FileHandler, Formatter, StreamHandler, getLogger


def setup_logger(filename="log.log"):
    """
    Example:
        setup_logger(filename="test.log") 
        logger = getLogger(__name__)
    """
    logger = getLogger(__name__)
    logger.setLevel(DEBUG)
    logger.propagate = False

    formatter = Formatter("%(asctime)s %(levelname)-7s %(funcName)-7s %(message)s")

    s_handler = StreamHandler()
    s_handler.setFormatter(formatter)
    s_handler.setLevel(DEBUG)
    logger.addHandler(s_handler)

    f_handler = FileHandler(filename=filename)
    f_handler.setFormatter(formatter)
    f_handler.setLevel(DEBUG)
    logger.addHandler(f_handler)

    return logger


if __name__ == "__main__":
    setup_logger()
    logger = getLogger(__name__)

    logger.debug("debug message")
    logger.info("info message")
    logger.warning("warn message")
    logger.error("error message")
