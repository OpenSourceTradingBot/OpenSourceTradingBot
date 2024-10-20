from utils.market import calculate_time_interval
from utils import indicators

ONE_HOUR_RSI_THRESHOLD = 60
FOUR_HOUR_RSI_THRESHOLD = 60
STOP_LOSS_PERCENTAGE_THRESHOLD = -2.7

def rsi_test(last_prices: list[float]) -> bool:
    """
    Tests if the Relative Strength Index (RSI) values for the last hour and four hours
    are both above the specified thresholds.

    Args:
        last_prices (list[float]): A list of historical prices, ordered from most recent to oldest.

    Returns:
        True if both RSI values are above the thresholds, False otherwise.
    """

    one_hour_prices = last_prices[:calculate_time_interval("1h")]
    four_hour_prices = last_prices[:calculate_time_interval("4h")]

    rsi_1h = indicators.rsi(one_hour_prices)
    rsi_4h = indicators.rsi(four_hour_prices)

    return rsi_1h > ONE_HOUR_RSI_THRESHOLD and rsi_4h > FOUR_HOUR_RSI_THRESHOLD

def stop_loss(trades_data: list[dict], last_prices: list[float]) -> bool:
    """
    Determines if a stop-loss condition has been met.

    Args:
        trades: A list of trade dictionaries, each containing relevant trade information.
        last_prices: A list of the latest prices corresponding to each trade.

    Returns:
        True if the stop-loss condition is met, False otherwise.
    """

    percentage_difference = indicators.percentage_difference(trades_data[0].value_buyin, last_prices[0])

    return percentage_difference <= STOP_LOSS_PERCENTAGE_THRESHOLD

def tests(trades_data: list[object], last_prices: list) -> bool:
    """
    Tests if all the specified conditions are met for the given price data.

    Args:
        last_prices: A list of historical prices, ordered from most recent to oldest.

    Returns:
        True if all conditions are met, False otherwise.
    """

    test_functions = [rsi_test]

    if stop_loss(trades_data, last_prices):
        return True

    for test_func in test_functions:
        if not test_func(last_prices):
            return False

    return True
