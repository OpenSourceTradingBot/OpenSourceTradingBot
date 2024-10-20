from utils.database import close_session
from bots.binance_data_collection import main as binance_data_collector
from bots.rsi_example import main as rsi_example
from utils.logging import ExceptionLogger

def main():
    try:
        binance_data_collector.main()
        rsi_example.main()
    except Exception as e:
        ExceptionLogger().log_exception(e)
    finally:
        close_session()

if __name__ == "__main__":
    main()