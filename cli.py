import argparse
import sys
from bot.client import get_testnet_client
from bot.orders import place_market_order, place_limit_order
from bot.logging_config import logger

def main():
    parser = argparse.ArgumentParser(description="Binance Testnet Trading Bot CLI")
    
    # Global arguments
    parser.add_argument('--api-key', type=str, help='Binance Testnet API Key (or set BINANCE_TESTNET_API_KEY env var)')
    parser.add_argument('--api-secret', type=str, help='Binance Testnet API Secret (or set BINANCE_TESTNET_API_SECRET env var)')
    
    # Subparsers for different order types
    subparsers = parser.add_subparsers(dest='command', help='Commands', required=True)
    
    # Market Order Parser
    market_parser = subparsers.add_parser('market', help='Place a Market Order')
    market_parser.add_argument('symbol', type=str, help='Trading pair (e.g., BTCUSDT)')
    market_parser.add_argument('side', type=str, choices=['BUY', 'SELL', 'buy', 'sell'], help='BUY or SELL')
    market_parser.add_argument('quantity', type=float, help='Amount to buy/sell')

    # Limit Order Parser
    limit_parser = subparsers.add_parser('limit', help='Place a Limit Order')
    limit_parser.add_argument('symbol', type=str, help='Trading pair (e.g., BTCUSDT)')
    limit_parser.add_argument('side', type=str, choices=['BUY', 'SELL', 'buy', 'sell'], help='BUY or SELL')
    limit_parser.add_argument('quantity', type=float, help='Amount to buy/sell')
    limit_parser.add_argument('price', type=float, help='Price to buy/sell at')

    args = parser.parse_args()

    try:
        # Initialize client
        client = get_testnet_client(api_key=args.api_key, api_secret=args.api_secret)
        
        # Route command
        if args.command == 'market':
            place_market_order(client, args.symbol, args.side, args.quantity)
        elif args.command == 'limit':
            place_limit_order(client, args.symbol, args.side, args.quantity, args.price)
            
    except ValueError as ve:
        logger.error(f"Validation Error: {ve}")
        sys.exit(1)
    except Exception as e:
        logger.error("Program terminated due to an error.")
        sys.exit(1)

if __name__ == '__main__':
    main()