import logging
import os


def get_logger(name):

    os.makedirs("logs", exist_ok=True)

    logger = logging.getLogger(name)

    if not logger.handlers:

        logger.setLevel(logging.INFO)

        file_handler = logging.FileHandler(
            "logs/automation.log"
        )

        formatter = logging.Formatter(
            "%(asctime)s - %(levelname)s - %(message)s"
        )

        file_handler.setFormatter(formatter)

        logger.addHandler(file_handler)

    return logger