# ------------------------------
# Bot Configuration
# ------------------------------
# BOT_ID: The unique identifier for this bot instance. Used to track the bot in the system.
BOT_ID = 1  # Set to 1 as the default ID for this bot.

# BOT_NAME: The name of the bot. This is used for logging and identification purposes.
BOT_NAME = "RSI_example"  # The bot's name. Can be changed as needed.

# SYMBOL_ID: The unique identifier for the trading symbol (e.g., BTC, ETH, etc.).
SYMBOL_ID = 12  # Set to 12 as the default symbol ID. This should correspond to the asset you're trading.

# ------------------------------
# Trading Configuration
# ------------------------------
# CONSIDERED_TIME_FRAME: The time interval over which market data is considered (e.g., "1h", "4h", "1d").
CONSIDERED_TIME_FRAME = "4h"  # Set to 4 hours by default. This is the timeframe for technical indicators.

# TRADE_TEST_MODE: When set to True, the bot operates in test mode. In this mode, 
# the bot will execute trades regardless of whether all test conditions are met. 
TRADE_TEST_MODE = False  # Set to True for testing purposes.

# LIVE_TRADING: When set to True and `LIVE_TEST_TRADING` is set to False, the bot will execute live trades 
# using real money. This mode should be used with caution as it will perform real trades in the market.
# Ensure that all risk management and conditions are properly set before switching to this mode.
LIVE_TRADING = False  # Set to True when you're ready to execute live trades with actual funds.

# LIVE_TEST_TRADING: When set to True, and `LIVE_TRADING` is also True, the bot will execute real Binance 
# trades, but using the `create_test_order()` method. This allows you to simulate live trading behavior 
# while avoiding any real financial transactions. It’s ideal for debugging and ensuring the bot’s logic 
# works as expected in a live environment without risking actual capital.
LIVE_TEST_TRADING = True  # Set to True for safe testing of live trades using Binance's test environment (no real money involved).

# BUY_TRADE_ALLOCATION_PERCENT: The percentage of your available balance to allocate for each buy trade.
# This setting controls how much of your balance will be used when executing a buy order.
BUY_TRADE_ALLOCATION_PERCENT = 100  # Set to 100% by default, meaning all available funds are used for each buy trade.

# SELL_TRADE_ALLOCATION_PERCENT: The percentage of your available balance to allocate for each sell trade.
# This setting controls how much of your balance will be used when executing a sell order.
SELL_TRADE_ALLOCATION_PERCENT = 100  # Set to 100% by default, meaning all available funds are used for each sell trade.
