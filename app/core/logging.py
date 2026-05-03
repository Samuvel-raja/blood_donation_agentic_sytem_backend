import logging
import os
from logging.handlers import RotatingFileHandler

LOGS_DIR = "logs"
os.makedirs(LOGS_DIR, exist_ok=True)

LOG_FILE_PATH = os.path.join(LOGS_DIR, "app.log")

class SafeFormatter(logging.Formatter):
    def format(self, record):
        if not hasattr(record, "trace_id"):
            record.trace_id = "-"
        if not hasattr(record, "code"):
            record.code = "-"
        if not hasattr(record, "err_message"):
            record.err_message = "-"
        return super().format(record)

file_handler = RotatingFileHandler(
    LOG_FILE_PATH,
    maxBytes=10 * 1024 * 1024,
    backupCount=3,
    encoding="utf-8"
)

console_handler = logging.StreamHandler()

formatter = SafeFormatter(
    "%(asctime)s | %(levelname)s | %(name)s | %(message)s | %(err_message)s | %(trace_id)s "
)

file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

logger = logging.getLogger()
logger.setLevel(logging.INFO)

if not logger.handlers:
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)