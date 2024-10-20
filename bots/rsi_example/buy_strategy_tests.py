from utils.market import calculate_time_interval
from utils.indicators import rsi

ONE_HOUR_RSI_THRESHOLD = 40
FOUR_HOUR_RSI_THRESHOLD = 40

def rsi_test(last_prices: list[float]) -> bool:
    """
    Tests if the Relative Strength Index (RSI) values for the last hour and four hours
    are both below 100.

    Args:
        last_prices: A list of historical prices, ordered from most recent to oldest.

    Returns:
        True if both RSI values are below 100, False otherwise.
    """
    one_hour_prices = last_prices[:calculate_time_interval("1h")]
    four_hour_prices = last_prices[:calculate_time_interval("4h")]

    rsi_1h = rsi(one_hour_prices)
    rsi_4h = rsi(four_hour_prices)

    return rsi_1h < ONE_HOUR_RSI_THRESHOLD and rsi_4h < FOUR_HOUR_RSI_THRESHOLD

def tests(last_prices: list) -> bool:
    """
    Tests if all the specified conditions are met for the given price data.

    Args:
        last_prices: A list of historical prices, ordered from most recent to oldest.

    Returns:
        True if all conditions are met, False otherwise.
    """

    test_functions = [rsi_test]

    for test_func in test_functions:
        if not test_func(last_prices):
            return False

    return True