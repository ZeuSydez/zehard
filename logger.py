import logging
from datetime import datetime
import os

class MyLogger:
    def __init__(self, log_dir='log', level=logging.INFO):
        self.log_dir = log_dir
        self.level = level
        self.logger = self.setup_logger()
        self.INFO = logging.INFO
        self.WARNING = logging.WARNING
        self.ERROR = logging.ERROR
        self.CRITICAL = logging.CRITICAL

    def setup_logger(self):
        logger = logging.getLogger('my_logger')
        logger.setLevel(self.level)
        
        return logger

    def log(self, message, level=logging.INFO, separator=None):
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        current_date = datetime.now().strftime('%Y-%m-%d')
        log_file = os.path.join(self.log_dir, f'{current_date}.log')
        
        if not os.path.exists(log_file):
            file_handler = logging.FileHandler(log_file)
            file_handler.setLevel(self.level)
            file_handler.setFormatter(formatter)
            self.logger.addHandler(file_handler)
        
        if separator:
            self.logger.info(separator)
        
        if level == logging.DEBUG:
            self.logger.debug(message)
        elif level == logging.INFO:
            self.logger.info(message)
        elif level == logging.WARNING:
            self.logger.warning(message)
        elif level == logging.ERROR:
            self.logger.error(message)
        elif level == logging.CRITICAL:
            self.logger.critical(message)
