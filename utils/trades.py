from utils.database import get_session
from utils.indicators import percentage_difference
from utils.binance_api import BinanceClient
from utils.symbols import get_symbol_by_id
from models.trades import Trades
from sqlalchemy import desc
from decimal import Decimal
from utils.logging import ExceptionLogger

def get_trades(bot_id: int) -> list[Trades]:
    """
    Retrieves a list of trades associated with the specified bot ID.

    Args:
        bot_id (int): ID of the bot for which to retrieve trades.

    Returns:
        list[Trades]: List of Trades objects representing the retrieved trades.
    """

    try:
        trade_data = get_session().query(Trades) \
            .filter(Trades.bot_id == bot_id) \
            .order_by(desc(Trades.id)) \
            .all()
        return trade_data
    except Exception as e:
        ExceptionLogger().log_exception(e)
        return []
    
def get_last_trade_id(bot_id: int) -> int:
    """Retrieves the ID of the last trade associated with the given bot.

    Args:
        bot_id: The ID of the bot.

    Returns:
        The ID of the last trade, or 0 if no trades are found.
    """

    last_trade = get_session().query(Trades).filter(Trades.bot_id == bot_id).order_by(desc(Trades.id)).first()
    if last_trade:
        return last_trade.market_id_sellout or last_trade.market_id_buyin
    else:
        return 0

def execute_buy_order(bot_id: int, symbol_id: int, live_trading: bool, trade_allocation_percent: int, live_test_trading: bool, market_data: list[object]) -> Trades:
    """Executes a buy order based on provided market data.

    Args:
        bot_id: The ID of the trading bot.
        symbol_id: The ID of the traded symbol.
        market_data: A list of market data objects.

    Returns:
        The created Trades object.

    Raises:
        ValueError: If the market data is empty or invalid.
    """

    if not market_data:
        raise ValueError("Market data is empty.")

    market_data = market_data[-1]

    trade = Trades(
        bot_id=bot_id,
        symbol_id=symbol_id,
        market_id_buyin=market_data.id,
        value_buyin=market_data.last_price,
        datetime_buyin=market_data.created_at
    )

    get_session().add(trade)
    get_session().commit()
    if live_trading:
        try:
            BinanceClient().create_market_order(get_symbol_by_id(symbol_id), trade_allocation_percent, 'buy', live_test_trading)
        except Exception as e:
            ExceptionLogger().log_exception(e)

    return trade

def execute_sell_order(trades_data:list[object], market_data:list[object], live_trading: bool, trade_allocation_percent: int, live_test_trading: bool) -> Trades:
    """Executes a sell order based on the provided trades and market data.

    Args:
        trades_data: A list of Trades objects.
        market_data: A list of market data objects.

    Returns:
        The updated Trades object.

    Raises:
        ValueError: If there are no trades or the market data is empty or invalid.
    """

    if not trades_data or not market_data:
        raise ValueError("Trades or market data are empty or invalid.")

    last_trade = trades_data[0]
    last_market_data = market_data[-1]

    last_trade.market_id_sellout = last_market_data.id
    last_trade.value_sellout = last_market_data.last_price
    last_trade.datetime_sellout = last_market_data.created_at
    last_trade.percentage_difference = percentage_difference(last_trade.value_buyin, last_market_data.last_price)
    if len(trades_data) == 1:
        last_trade.total_percentage_change = last_trade.percentage_difference
    else:
        last_trade.total_percentage_change = trades_data[1].total_percentage_change + last_trade.percentage_difference
    
    get_session().commit()

    if live_trading:
        try:
            BinanceClient().create_market_order(get_symbol_by_id(last_trade.symbol_id), trade_allocation_percent, 'sell', live_test_trading)
        except Exception as e:
            ExceptionLogger().log_exception(e)

    return last_trade
