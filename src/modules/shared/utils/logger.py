import logging

# Logger is an object that manages all the logging events
logger = logging.getLogger()

# Formatter defines the output format of the log record
formatter = logging.Formatter(
    fmt="%(asctime)s - %(levelname)s - %(message)s"
)

# Handler defines where the log records are going to be shipped
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)

logger.addHandler(stream_handler)
logger.setLevel(logging.INFO)
