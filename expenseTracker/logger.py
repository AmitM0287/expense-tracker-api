import os
import logging
from logging.handlers import RotatingFileHandler


class Logger:
    ''' This is used to log information into a log file '''
    _ref = None
    
    def __init__(self):
        Logger._ref = self
        self._logger = self.__initializeLoggerConf()
    
    @classmethod
    def initialize(cls):
        if cls._ref is None:
            cls._ref = cls()
        return cls._ref
    
    def __initializeLoggerConf(self):
        # configure log rotation and logging format
        formatter = logging.Formatter(os.getenv('LOGGER_FORMAT'), datefmt=os.getenv('DATE_FORMAT'))
        handler = RotatingFileHandler(filename='expenseTracker.log', maxBytes=int(os.getenv('MAX_BYTES')), backupCount=int(os.getenv('BACKUP_COUNT')))
        handler.setFormatter(formatter)
        # configure logger to use the rotating file handler
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.INFO)
        logger.addHandler(handler)
        return logger
    
    def _logInfo(self, processTime, msg, status):
        self._logger.info(f'Processing Time: {processTime} | Message: {msg} | Status: {status}')
    
    def _logException(self, exc):
        self._logger.exception(f'Exception Type: {type(exc)} | Exception: {exc}')
    
    def _logError(self, error):
        self._logger.error(f'Exception Type: {type(error)} | Error: {error}')


# initialize logger
Logger.initialize()
