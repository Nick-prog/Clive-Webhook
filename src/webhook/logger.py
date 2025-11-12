import logging
import os
from logging.handlers import RotatingFileHandler

LOG_PATH = os.path.join(os.getcwd(), 'logs')
if not os.path.isdir(LOG_PATH):
    try:
        os.makedirs(LOG_PATH, exist_ok=True)
    except Exception:
        pass

def _build_logger(name: str = 'clive_webhook') -> logging.Logger:
    logger = logging.getLogger(name)
    if logger.handlers:
        return logger
    logger.setLevel(os.getenv('CLIVE_LOG_LEVEL', 'INFO'))
    fmt = logging.Formatter('%(asctime)s [%(levelname)s] %(name)s:%(lineno)d - %(message)s')
    fh = RotatingFileHandler(os.path.join(LOG_PATH, 'clive_webhook.log'), maxBytes=5_000_000, backupCount=3)
    fh.setFormatter(fmt)
    logger.addHandler(fh)
    ch = logging.StreamHandler()
    ch.setFormatter(fmt)
    logger.addHandler(ch)
    return logger

logger = _build_logger()
