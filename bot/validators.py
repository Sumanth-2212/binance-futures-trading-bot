def validate_symbol(symbol: str) -> str:
    symbol = symbol.upper()
    if not symbol.isalnum():
        raise ValueError(f"Invalid symbol format: {symbol}. Must be alphanumeric (e.g., BTCUSDT).")
    return symbol

def validate_side(side: str) -> str:
    side = side.upper()
    valid_sides = ['BUY', 'SELL']
    if side not in valid_sides:
        raise ValueError(f"Invalid side: {side}. Must be one of {valid_sides}.")
    return side

def validate_order_type(order_type: str) -> str:
    order_type = order_type.upper()
    valid_types = ['MARKET', 'LIMIT']
    if order_type not in valid_types:
        raise ValueError(f"Invalid order type: {order_type}. Must be one of {valid_types}.")
    return order_type

def validate_quantity(quantity: float) -> float:
    if quantity <= 0:
        raise ValueError(f"Invalid quantity: {quantity}. Must be greater than 0.")
    return quantity

def validate_price(price: float, order_type: str) -> float:
    if order_type.upper() == 'LIMIT':
        if price is None or price <= 0:
            raise ValueError("A valid price greater than 0 is required for LIMIT orders.")
    return price