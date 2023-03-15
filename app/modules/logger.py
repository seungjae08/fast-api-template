import os
import logging


def initialize_logging(logging_name: str, level: str):
    pid = os.getpid()
    logger = logging.getLogger(logging_name)
    match level:
        case "INFO":
            logger.setLevel(logging.INFO)
        case "DEBUG":
            logger.setLevel(logging.DEBUG)
        case "WARN":
            logger.setLevel(logging.WARN)
        case "ERROR":
            logger.setLevel(logging.ERROR)

    log_format = f"%(asctime)s %(name)s {pid} %(levelname)s : %(message)s"
    formatter = logging.Formatter(log_format)

    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)

    file_handler = logging.FileHandler(f"./logs/{pid}.log")
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

