import os
import logging
from logging.handlers import RotatingFileHandler

# Configure log rotation and logging format
formatter = logging.Formatter(os.getenv('LOGGER_FORMAT'), datefmt=os.getenv('DATE_FORMAT'))
handler = RotatingFileHandler(filename='expenseTracker.log', maxBytes=int(os.getenv('MAX_BYTES')), backupCount=int(os.getenv('BACKUP_COUNT')))
handler.setFormatter(formatter)

# Configure root logger to use the rotating file handler
logger = logging.getLogger()
logger.setLevel(logging.INFO)
logger.addHandler(handler)
