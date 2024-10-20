from tqdm import tqdm
from utils.trades import get_last_trade_id
from utils.market import calculate_time_interval, retrieve_backtest_market_data
from bots.rsi_example import config, main as rsi_example
from utils.logging import ExceptionLogger

def main():
    """
    Main function to run the backtesting process for the RSI trading strategy.
    
    Raises:
        ValueError: If no trade ID is found, invalid time frame is provided, or
                    no market data is available for backtesting.
        Exception: Any errors encountered during the backtest execution.
    """
    try:
        last_trade_id = get_last_trade_id(config.BOT_ID)
        if last_trade_id is None:
            raise ValueError("No last trade ID found.")

        considered_time = calculate_time_interval(config.CONSIDERED_TIME_FRAME)
        if considered_time <= 0:
            raise ValueError("Invalid considered time frame.")

        market_data = retrieve_backtest_market_data(last_trade_id, config.SYMBOL_ID, considered_time)
        if not market_data:
            raise ValueError("No market data found for backtesting.")

        iteration = 0
        upper = considered_time

        with tqdm(total=len(market_data), desc=f"{config.BOT_NAME} Backtesting Progress", unit="iterations") as pbar:
            while upper < len(market_data):
                try:
                    upper = iteration + considered_time
                    rsi_example.main(market_data[iteration:upper])
                    iteration += considered_time
                    pbar.update(considered_time)
                except Exception as e:
                    print(f"Error during RSI backtest execution for iteration {iteration}-{upper}: {e}")
                    ExceptionLogger().log_exception(e)
            
    except Exception as e:
        print(f"Error in backtest execution: {e}")
        ExceptionLogger().log_exception(e)
