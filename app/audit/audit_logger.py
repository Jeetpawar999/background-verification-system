import logging

logging.basicConfig(
    filename="audit.log",
    level=logging.INFO
)


def log_event(message):

    logging.info(message)