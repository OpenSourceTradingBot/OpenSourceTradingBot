
from utils import symbols, binance_api, market
from utils.logging import ExceptionLogger
from typing import List
from binance.exceptions import BinanceAPIException

def process_market_data(all_markets: List[dict], all_symbols: List[tuple]) -> None:
    """
    Processes market data and creates Market objects.
    Args:
        all_markets: A list of market data dictionaries.
        all_symbols: A list of Symbol objects.
    
    Returns:
        None
    """
    symbol_map = {symbol[0].symbol: symbol[0] for symbol in all_symbols}

    for market_data in all_markets:
        symbol = symbol_map.get(market_data['symbol'])
        if symbol:
            market.insert(symbol.id, market_data)

def main() -> None:
    """
    The main entry point for the script. Retrieves market data and symbols, then processes them.
    """
    try:
        binance_client = binance_api.BinanceClient()
        market_data = binance_client.get_market_data()
        symbols_data = symbols.get_all()

        process_market_data(market_data, symbols_data)

    except BinanceAPIException as e:
        print(f"Binance API error: {e}")
        ExceptionLogger().log_exception(e)

    except ConnectionError as e:
        ExceptionLogger().log_exception(e)
    
    except Exception as e:
        ExceptionLogger().log_exception(e)
