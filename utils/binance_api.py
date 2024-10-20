from binance.client import Client
import os
from typing import Dict
from utils.logging import ExceptionLogger
from binance.exceptions import BinanceAPIException

class BinanceClient:

    def __init__(self, api_key: str = os.getenv("BINANCE_API_KEY"), api_secret: str = os.getenv("BINANCE_API_SECRET")):
        """
        Initializes a Binance API client.

        Args:
            api_key (str): Your Binance API key.
            api_secret (str): Your Binance API secret.
        """

        self.client = Client(api_key, api_secret)

    def get_market_data(self) -> Dict:
        """
        Returns general statistics for the last 24 hours on Binance.

        Returns:
            Dict: A dictionary containing various 24-hour statistics.
        """

        return self.client.get_ticker()
    
    def calculate_trade_quantity(self, symbol: str, trade_allocation_percent: float) -> float:
        """
        Calculates the trade quantity based on the allocation percentage and ensures it meets the minimum lot size.

        Args:
            symbol (str): The trading pair symbol (e.g., 'BTCUSDT').
            trade_allocation_percent (float): The percentage of available balance to allocate for the trade (0-100).

        Returns:
            float: The calculated trade quantity that adheres to the minimum lot size requirements.

        Raises:
            ValueError: If the calculated quantity is below the minimum allowed lot size or another issue arises.
        """
        try:
            symbol_info = self.client.get_symbol_info(symbol)
            free_quote_asset_value = float(self.client.get_asset_balance(symbol_info['quoteAsset'])['free'])
            exchange_info = self.client.get_exchange_info()
            minimum_order_qty = None
            for symbol_info in exchange_info['symbols']:
                if symbol_info['symbol'] == symbol:
                    for filter_info in symbol_info['filters']:
                        if filter_info['filterType'] == 'LOT_SIZE':
                            minimum_order_qty = float(filter_info['minQty'])
                            break
            if minimum_order_qty is None:
                raise ValueError(f"Could not find minimum order quantity for symbol {symbol}.")

            ask_price = float(self.client.get_ticker(symbol=symbol)['askPrice'])
            base_asset_value = free_quote_asset_value / ask_price
            trade_quantity = round(base_asset_value * (trade_allocation_percent / 100), 8)
            trade_quantity_str = "{:.8f}".format(trade_quantity)

            if float(trade_quantity_str) < minimum_order_qty:
                raise ValueError(f"""
                    Error: The calculated trade quantity for {symbol} is below the minimum allowed lot size.
                    The minimum trade size is {minimum_order_qty} {symbol}. 
                    Please adjust the trade quantity to be at least {minimum_order_qty} {symbol}.
                """)

            return float(trade_quantity_str)

        except Exception as e:
            print(f"Error calculating trade quantity for {symbol}: {e}")
            ExceptionLogger().log_exception(e)
            raise
    
    def create_market_order(
        self,
        symbol: str,
        trade_allocation_percent: float,
        side: str,
        test: bool = False
    ) -> None:
        """
        Creates a market order with the given parameters.

        Parameters:
        - symbol (str): Trading pair symbol, e.g., 'BTCUSDT'
        - trade_allocation_percent (float): Percentage of available balance to allocate.
        - side (str): 'buy' or 'sell'.
        - test (bool): If True, creates a test order instead of an actual order.

        Raises:
        - ValueError: If the side is invalid.
        """
        try:
            if side.lower() == 'buy':
                order_side = Client.SIDE_BUY
            elif side.lower() == 'sell':
                order_side = Client.SIDE_SELL
            else:
                raise ValueError("Invalid side. Must be 'buy' or 'sell'.")

            params = {
                'symbol': symbol.symbol,
                'side': order_side,
                'type': Client.ORDER_TYPE_MARKET,
                'quantity': self.calculate_trade_quantity(symbol.symbol, trade_allocation_percent)
            }

            if test:
                self.client.create_test_order(**params)
            else:
                self.client.create_order(**params)
        
        except BinanceAPIException as e:
            print(f"Binance API error: {e}")
            ExceptionLogger().log_exception(e)

        except ValueError as ve:
            ExceptionLogger().log_exception(ve)

        except Exception as e:
            ExceptionLogger().log_exception(e)
