import logging
from dotenv import load_dotenv
import os

class ExceptionLogger:
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.DEBUG)
        load_dotenv()
        file_handler = logging.FileHandler(os.getenv("EXCEPTION_LOG_FILE_NAME"))
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)
        self.logger.addHandler(file_handler)

    def log_exception(self, exception):
        self.logger.exception("An exception occurred:", exc_info=exception)
