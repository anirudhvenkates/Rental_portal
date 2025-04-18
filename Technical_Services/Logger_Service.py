import logging
from logging.handlers import TimedRotatingFileHandler

class LoggingService:
    def __init__(self, username: str):
        # each user gets a LoggerAdapter that tags every record with their name
        self._base_logger = logging.getLogger("app")  
        self._ensure_handler()
        self.logger = logging.LoggerAdapter(self._base_logger, {"user": username})

    def _ensure_handler(self):
        if not any(isinstance(h, TimedRotatingFileHandler) for h in self._base_logger.handlers):
            handler = TimedRotatingFileHandler("logs/app.log", when="midnight", backupCount=4)
            fmt = "%(asctime)s [%(user)s] %(levelname)s: %(message)s"
            handler.setFormatter(logging.Formatter(fmt))
            self._base_logger.addHandler(handler)
            self._base_logger.setLevel(logging.INFO)

    # Convenience methods
    def info(self, msg, **kw):
        self.logger.info(msg, **kw)
    def debug(self, msg, **kw):
        self.logger.debug(msg, **kw)
    def warning(self, msg, **kw):
        self.logger.warning(msg, **kw)
    def error(self, msg, **kw):
        self.logger.error(msg, **kw)
