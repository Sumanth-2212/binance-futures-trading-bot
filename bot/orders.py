from binance.exceptions import BinanceAPIException
from bot.logging_config import logger
from bot.validators import (
    validate_symbol, 
    validate_side, 
    validate_quantity, 
    validate_price
)

def print_order_summary(order_response, order_type):
    """Formats and prints the exact output required by the assignment."""
    print("\n" + "="*40)
    print("✅ SUCCESS: Order Placed Successfully!")
    print("="*40)
    print("📋 ORDER RESPONSE DETAILS:")
    print(f"  • Order ID:     {order_response.get('orderId')}")
    print(f"  • Status:       {order_response.get('status')}")
    print(f"  • Symbol:       {order_response.get('symbol')}")
    print(f"  • Side:         {order_response.get('side')}")
    print(f"  • Type:         {order_type}")
    print(f"  • Executed Qty: {order_response.get('executedQty')}")
    
    # avgPrice is sometimes returned in futures, otherwise we can show price
    avg_price = order_response.get('avgPrice')
    if avg_price and float(avg_price) > 0:
        print(f"  • Avg Price:    {avg_price}")
    elif order_response.get('price') and float(order_response.get('price')) > 0:
        print(f"  • Target Price: {order_response.get('price')}")
        
    print("="*40 + "\n")


def place_market_order(client, symbol: str, side: str, quantity: float):
    symbol = validate_symbol(symbol)
    side = validate_side(side)
    quantity = validate_quantity(quantity)

    logger.info(f"REQUEST: Placing MARKET {side} order for {quantity} {symbol} on FUTURES...")
    
    try:
        # Notice we are using futures_create_order now
        order = client.futures_create_order(
            symbol=symbol,
            side=side,
            type='MARKET',
            quantity=quantity
        )
        logger.info(f"RESPONSE: Market order successful! Order ID: {order.get('orderId')}")
        print_order_summary(order, "MARKET")
        return order
        
    except BinanceAPIException as e:
        logger.error(f"Binance API Error: {e}")
        print(f"\n❌ FAILURE: Binance API Error - {e}\n")
        raise
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        print(f"\n❌ FAILURE: Unexpected error - {e}\n")
        raise


def place_limit_order(client, symbol: str, side: str, quantity: float, price: float):
    symbol = validate_symbol(symbol)
    side = validate_side(side)
    quantity = validate_quantity(quantity)
    price = validate_price(price, 'LIMIT')

    logger.info(f"REQUEST: Placing LIMIT {side} order for {quantity} {symbol} at {price} on FUTURES...")
    
    try:
        # Notice we are using futures_create_order now
        order = client.futures_create_order(
            symbol=symbol,
            side=side,
            type='LIMIT',
            timeInForce='GTC',
            quantity=quantity,
            price=str(price)
        )
        logger.info(f"RESPONSE: Limit order successful! Order ID: {order.get('orderId')}")
        print_order_summary(order, "LIMIT")
        return order
        
    except BinanceAPIException as e:
        logger.error(f"Binance API Error: {e}")
        print(f"\n❌ FAILURE: Binance API Error - {e}\n")
        raise
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        print(f"\n❌ FAILURE: Unexpected error - {e}\n")
        raise