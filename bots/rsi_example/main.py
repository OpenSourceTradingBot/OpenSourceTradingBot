from bots.rsi_example import config
from utils import market, trades
from bots.rsi_example.buy_strategy_tests import tests as buy_test
from bots.rsi_example.sell_strategy_tests import tests as sell_test

def main(market_data: list[object] = None) -> None:
    """Main function for executing the trading strategy."""
    if market_data == None:
        market_data = market.get_latest_market_data(config.SYMBOL_ID, config.CONSIDERED_TIME_FRAME)
    last_prices = market.extract_last_prices(market_data)
    if len(last_prices) <= market.calculate_time_interval(config.CONSIDERED_TIME_FRAME):
        trades_data = trades.get_trades(config.BOT_ID)
        if not trades_data:
            buy(market_data, last_prices)
        else:
            last_trade_sold = trades_data[0].market_id_sellout
            if last_trade_sold:
                buy(market_data, last_prices)
            else:
                sell(trades_data, market_data, last_prices)

def buy(market_data: list[object], last_prices: list) -> None:
    """
    Initiates a buy order based on the provided market data.

    Args:
        market_data (list[object]): list containing Market objects.
        last_prices (list): List containing historic price data.
    """
    if config.TRADE_TEST_MODE or buy_test(last_prices):
        trades.execute_buy_order(config.BOT_ID, config.SYMBOL_ID, config.LIVE_TRADING, config.BUY_TRADE_ALLOCATION_PERCENT, config.LIVE_TEST_TRADING, market_data)

def sell(trades_data:list[object], market_data:list[object], last_prices: list) -> None:
    """
    Initiates a sell order based on the provided trades and market data.

    Args:
        trades_data (list[object]): List of existing trade objects.
        market_data (list[object]): List containing marktet data objects.
        last_prices (list): List containing historic price data.

    """
    if config.TRADE_TEST_MODE or sell_test(trades_data, last_prices):
        trades.execute_sell_order(trades_data, market_data, config.LIVE_TRADING, config.SELL_TRADE_ALLOCATION_PERCENT, config.LIVE_TEST_TRADING)


