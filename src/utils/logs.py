import logging
import queue
from logging.handlers import QueueHandler, QueueListener, RotatingFileHandler


log_queue = queue.Queue(-1)


def setup_logging(debug_console: bool = False):
    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
    )

    handlers = []
    file_handler = RotatingFileHandler(
        "/app/src/logs/app.log",
        maxBytes=10_000_000,
        backupCount=5
    )
    file_handler.setFormatter(formatter)
    file_handler.setLevel(logging.INFO)
    handlers.append(file_handler)

    if debug_console:
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        console_handler.setLevel(logging.DEBUG)
        handlers.append(console_handler)


    queue_handler = QueueHandler(log_queue)

    root_logger = logging.getLogger('testTaskBot')
    root_logger.setLevel(logging.INFO)
    root_logger.addHandler(queue_handler)

    listener = QueueListener(log_queue, *handlers)
    listener.start()
