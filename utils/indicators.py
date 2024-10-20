from utils.logging import ExceptionLogger

def percentage_difference(old_value:float, new_value:float) -> float:
    """Calculates the percentage difference between two values.

    Args:
        old_value: The original value.
        new_value: The new value.

    Returns:
        The percentage difference between the two values, negative if new_value is less than old_value.
    """

    if old_value == 0 or new_value == 0:
        raise ValueError("Cannot calculate percentage difference with zero values.")

    difference = new_value - old_value
    average = (old_value + new_value) / 2
    percentage_difference = (difference / average) * 100

    return round(percentage_difference, 10)

def rsi(price_data: list) -> float:
    """Calculates the Relative Strength Index (RSI) of a given price series.

    Args:
        price_data: A list of price data points.

    Returns:
        The calculated RSI value, or 0 if there is insufficient data.
    """
    try:
        deltas = [price_data[i] - price_data[i - 1] for i in range(1, len(price_data))]
        gains = [d if d >= 0 else 0 for d in deltas]
        losses = [-d if d < 0 else 0 for d in deltas]
        if len(gains) == 0 or len(losses) == 0:
            return 0

        avg_gain = sum(gains) / len(gains)
        avg_loss = sum(losses) / len(losses)

        rs = avg_gain / avg_loss if avg_loss != 0 else 0
        rsi = 100 - (100 / (1 + rs))

        return rsi
    
    except IndexError as e:
        ExceptionLogger().log_exception(f"Index error in RSI calculation: {e}")
    except ZeroDivisionError as e:
        ExceptionLogger().log_exception(f"Zero division in RSI calculation: {e}")
    except Exception as e:
        ExceptionLogger().log_exception(f"Unexpected error in RSI calculation: {e}")