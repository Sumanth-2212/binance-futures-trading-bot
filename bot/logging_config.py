import logging
import os

def setup_logger():
    # Ensure the logs directory exists
    os.makedirs('logs', exist_ok=True)

    logger = logging.getLogger('TradingBot')
    logger.setLevel(logging.INFO)

    # File handler (appends logs continuously)
    file_handler = logging.FileHandler('logs/trading_bot.log')
    file_handler.setLevel(logging.INFO)

    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)

    # Format
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    # Avoid duplicate logs if called multiple times
    if not logger.handlers:
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

    return logger

logger = setup_logger()