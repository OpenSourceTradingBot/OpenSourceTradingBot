from bots.rsi_example import backtester as rsi_backtest
from utils.logging import ExceptionLogger
from utils.database import close_session

def main():
    try:
        rsi_backtest.main()
    except Exception as e:
        ExceptionLogger().log_exception(e)
    finally:
        close_session()

if __name__ == "__main__":
    main()