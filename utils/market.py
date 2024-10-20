from typing import Dict
from sqlalchemy import desc
from sqlalchemy.exc import SQLAlchemyError
from dotenv import load_dotenv
import os
from utils.logging import ExceptionLogger
from utils.database import get_session
from models.market import Market
import datetime


def calculate_time_interval(time_unit: str) -> int:
    """Calculates the time interval in seconds based on the given time unit.

    Args:
        time_unit (str): The time unit, one of 'm' (minutes), 'h' (hours), 'd' (days), or 'w' (weeks).

    Returns:
        int: The calculated time interval in seconds. If the time unit is invalid, returns 0.
    """

    load_dotenv()
    iteration_time_seconds = int(os.getenv("ITERATION_TIME"))

    valid_time_units = {'m', 'h', 'd', 'w'}

    if time_unit[-1] not in valid_time_units:
        raise ValueError(f"Invalid time unit '{time_unit}'. Valid units are 'm', 'h', 'd', or 'w'.")

    time_intervals = {
        'm': 60,
        'h': 3600,
        'd': 86400,
        'w': 604800,
    }

    interval_seconds = time_intervals.get(time_unit[1], 0)
    return int(time_unit[0]) * (interval_seconds // iteration_time_seconds)

def get_latest_market_data(symbol_id: int, considered_time_frame: str = "1w") -> list[Market]:
    """Retrieves the most recent market data for a given symbol.

    Args:
        symbol_id (int): The unique identifier of the symbol.
        considered_time_frame (str, optional): The considered time frame of results to return.
            Defaults to 1w.

    Returns:
        list[Market]: A list of Market objects containing the latest market data.
            If no data is found or an error occurs, an empty list will be returned.
    """

    try:
        max_results = calculate_time_interval(considered_time_frame)
        market_data = get_market_data_by_symbol_id(symbol_id, max_results)
    except SQLAlchemyError as e:
        ExceptionLogger().log_exception(e)
        market_data = []

    return market_data

def retrieve_backtest_market_data(market_id: int, symbol_id: str, considered_time: int) -> list[Market]:
    """Retrieves market data for backtesting, considering the specified symbol and time frame.

    Args:
        market_id: The ID of the market data point to use as a reference.
        symbol_id: The symbol of the market data to retrieve.
        considered_time: The number of data points to retrieve (including the reference point).

    Returns:
        A list of Market objects containing the retrieved market data,
        sorted in chronological order with the reference point at the beginning.

    Raises:
        SQLAlchemyError: If an error occurs during database interaction.
    """
    try:
        if market_id == 0:
            market_data = get_market_data_by_symbol_id(symbol_id)
            return market_data

        after_market_data = get_session().query(Market) \
            .filter(Market.symbol_id == symbol_id, Market.id >= market_id) \
            .all()
        
        before_market_data = get_session().query(Market) \
            .filter(Market.symbol_id == symbol_id, Market.id < market_id) \
            .order_by(desc(Market.id)) \
            .limit(considered_time - 2) \
            .all()[::-1]

        return before_market_data + after_market_data
    
    except SQLAlchemyError as e:
        ExceptionLogger().log_exception(e)
        return []

def extract_last_prices(market_data: list) -> list:
    """Extracts the last prices from a list of market data objects.

    Args:
        market_data: A list of market data objects, each containing a 'last_price' attribute.

    Returns:
        A list of last prices extracted from the market data, or an empty list if an error occurs.
    """

    try:
        return [data.last_price for data in market_data]
    except AttributeError as e:
        ExceptionLogger().log_exception(e)
        return []
    

def extract_created_at(market_data: list) -> list:
    """Extracts the last prices from a list of market data objects.

    Args:
        market_data: A list of market data objects, each containing a 'last_price' attribute.

    Returns:
        A list of last prices extracted from the market data, or an empty list if an error occurs.
    """

    try:
        return [data.created_at for data in market_data]
    except AttributeError as e:
        ExceptionLogger().log_exception(e)
        return []

def get_market_data_by_symbol_id(symbol_id: int, limit: int = None) -> list[Market]:
    """Retrieves market data for a given symbol ID, ordered by the most recent entries.

    Args:
        symbol_id: The symbol ID to query.
        limit: The number of records to retrieve (optional).

    Returns:
        A list of Market objects representing the market data, or an empty list if an error occurs.
    """
    try:
        query = get_session().query(Market).filter(Market.symbol_id == symbol_id)
        query = query.order_by(desc(Market.id))
        if limit:
            query = query.limit(limit)
        market_data = query.all()
        market_data.reverse()

        return market_data

    except SQLAlchemyError as e:
        ExceptionLogger().log_exception(e)
        return []


def insert(symbol_id: int, market_data: Dict[str, float]) -> Market:
    """Inserts market data into the database.

    Args:
        symbol_id (int): The symbol ID of the market data.
        market_data (Dict[str, float]): A dictionary containing the market data.

    Returns:
        Market: The created Market object.

    Raises:
        ValueError: If a required key is missing from market data or an error occurs during insertion.
    """

    try:
        market = Market(
            symbol_id=symbol_id,
            price_change=market_data["priceChange"],
            price_change_percent=market_data["priceChangePercent"],
            weighted_avg_price=market_data["weightedAvgPrice"],
            prev_close_price=market_data["prevClosePrice"],
            last_price=market_data["lastPrice"],
            last_qty=market_data["lastQty"],
            bid_price=market_data["bidPrice"],
            bid_qty=market_data["bidQty"],
            ask_price=market_data["askPrice"],
            ask_qty=market_data["askQty"],
            open_price=market_data["openPrice"],
            high_price=market_data["highPrice"],
            low_price=market_data["lowPrice"],
            volume=market_data["volume"],
            quote_volume=market_data["quoteVolume"],
            open_time=market_data["openTime"],
            close_time=market_data["closeTime"],
            first_id=market_data["firstId"],
            last_id=market_data["lastId"],
            count=market_data["count"],
            created_at=datetime.datetime.now()
        )
        get_session().add(market)
        get_session().commit()

        return market

    except KeyError as e:
        ExceptionLogger().log_exception(e)
    except Exception as e:
        ExceptionLogger().log_exception(e)