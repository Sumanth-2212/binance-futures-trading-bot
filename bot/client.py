import os
from dotenv import load_dotenv
from binance.client import Client
from bot.logging_config import logger

# This line is crucial: it loads the variables from your .env file
load_dotenv()

def get_testnet_client(api_key: str = None, api_secret: str = None) -> Client:
    """
    Initializes and returns a Binance Client pointed at the Testnet.
    Falls back to environment variables if keys are not explicitly passed.
    """
    key = api_key or os.getenv('BINANCE_TESTNET_API_KEY')
    secret = api_secret or os.getenv('BINANCE_TESTNET_API_SECRET')

    if not key or not secret:
        logger.error("API Key and Secret must be provided.")
        raise ValueError("Missing Binance API Key or Secret.")

    logger.info("Initializing Binance Testnet Client...")
    client = Client(key, secret, testnet=True)
    return client