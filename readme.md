# Open Source Trading Bot

## Description
The Open Source Trading Bot is a robust framework for developers to rapidly create, implement, and backtest custom algorithmic trading strategies. This project provides a clear path for collecting, storing, and analyzing market data, enabling the execution of real-time trades based on defined criteria.

## Table of Contents
- [Disclaimer](#disclaimer)
- [Key Features](#key-features)
- [Getting Started](#getting-started)
- [Configuration](#configuration)
- [Main Execution Flow](#main-execution-flow)
- [RSI Example Bot](#rsi-example-bot)
- [RSI Example Bot Configuration](#rsi-example-bot-configuration)
- [Backtesting](#backtesting)
- [Example Usage](#example-usage)
- [Conclusion](#conclusion)
- [Contribution Guidelines](#contribution-guidelines)
- [License Information](#license-information)
- [Contact Information](#contact-information)

## Disclaimer
The Open Source Trading Bot is intended for educational and informational purposes only. By using this software, you acknowledge and agree to the following:

- **No Financial Responsibility:** The developer(s) of this project are not responsible for any financial losses or damages incurred as a result of using this trading bot or any strategies implemented within it. Trading cryptocurrencies involves substantial risk, and you should only invest what you can afford to lose.
- **No Guarantees:** There are no guarantees of profit or success when using this bot. Performance may vary based on market conditions and individual trading strategies.
- **Do Your Own Research:** It is essential to conduct thorough research and consider your financial situation and risk tolerance before engaging in any trading activities.
- **Third-Party Services:** This bot interacts with third-party services (e.g., Binance API). Any issues or downtime experienced with these services are outside the control of the developer(s) and should be addressed directly with the service provider.

By proceeding with the use of this bot, you acknowledge that you understand the risks involved and accept full responsibility for your trading activities.

## Key Features
- **Algorithmic Trading:** Easily implement and customize trading strategies tailored to your preferences. The bot supports various indicators and conditions, allowing you to automate trading decisions based on technical analysis.
- **Backtesting Capabilities:** Evaluate your strategies against historical market data to refine performance before deploying them live. The backtesting module enables you to simulate trades and analyze results, helping you to optimize parameters and understand potential outcomes.
- **Python-Friendly:** Designed for developers familiar with Python, offering straightforward modification options. The codebase is modular, making it easy to add new features, strategies, or integrate additional data sources without extensive rewrites.
- **Data Collection and Management:** The bot includes a robust data collection module that retrieves real-time market data from the Binance API. Historical data is stored in a database for easy access, enabling effective analysis and strategy development.
- **Customizable Risk Management:** Implement your risk management rules with flexible options for stop-loss and take-profit settings. You can adjust parameters based on market conditions or personal risk tolerance to safeguard your investments.
- **Multi-Strategy Support:** Run multiple trading strategies simultaneously, allowing for diversified trading approaches. You can queue different bots to manage various assets or strategies, maximizing trading opportunities.
- **Logging and Monitoring:** Comprehensive logging features capture all bot activities, including trades executed, errors encountered, and market data fetched. This functionality allows for easy troubleshooting and performance monitoring.
- **Community-Driven:** As an open-source project, the bot encourages contributions from the community. You can share strategies, improvements, and insights with other developers, fostering collaboration and innovation.

## Getting Started

### Installation
Clone the repository and install the necessary dependencies.
```bash
git clone https://github.com/OpenSourceTradingBot/OpenSourceTradingBot.git
cd OpenSourceTradingBot
pip install -r requirements.txt
```

### Database Setup

Use Alembic to generate the database tables. Ensure you have a database configured in your `alembic.ini` file.

```bash
alembic upgrade head
```
### Scheduling

Set up a scheduler (e.g., cron job or Windows Task Scheduler) to run the bot. The default interval is set to 300 seconds (5 minutes).
## Configuration

To customize the trading bot, you will need to set up a configuration file (e.g., .env) with the following variables:

- `DATABASE_URL:` The connection URL for your database. Replace username, password, ipaddress, and database with your database credentials and information.  
  `DATABASE_URL="mysql+pymysql://username:password@ipaddress/database"`
  
- `BINANCE_API_KEY:` Your Binance API key. Obtain this from your Binance account settings to allow the bot to access your trading account.  
  `BINANCE_API_KEY="API_KEY"`
  
- `BINANCE_API_SECRET:` Your Binance API secret. This is required for secure API access and should be kept confidential.  
  `BINANCE_API_SECRET="API_SECRET"`
  
- `ITERATION_TIME:` The interval (in seconds) at which the bot runs its trading strategy. The default is set to 300 seconds (5 minutes).  
  `ITERATION_TIME=300`
  
- `EXCEPTION_LOG_FILE_NAME:` The filename for logging exceptions that occur during the execution of the bot. This file will help you debug issues.  
  `EXCEPTION_LOG_FILE_NAME="exception.log"`

## Main Execution Flow

- **main.py:** The core execution file that orchestrates the bot's operations.
- **Data Collection:** The `binance_data_collector` retrieves the latest market data from the Binance API and stores it in the database.
- **Strategy Execution:** The `RSI_example` bot processes the market data, assessing whether to buy or sell based on specified conditions.

## RSI Example Bot

- Allows for a customizable timeframe (e.g., last 4 weeks) to optimize data usage.
- Analyzes previous trades to determine buy/sell actions.
- Executes orders based on defined tests and updates the trades table accordingly.

## RSI Example Bot Configuration

In addition to the general configuration, you will need to specify settings for the `RSI_example` bot in your configuration file. Here are the key parameters:

- `BOT_ID:` The unique identifier for this bot instance. It is used to track the bot in the system.  
  `BOT_ID = 1`  # Default ID for this bot.
  
- `BOT_NAME:` The name of the bot, used for logging and identification purposes. You can change this as needed.  
  `BOT_NAME = "RSI_example"`
  
- `SYMBOL_ID:` The unique identifier for the trading symbol (e.g., BTC, ETH, etc.). This should correspond to the asset you're trading.  
  `SYMBOL_ID = 12`  # Default symbol ID.
  
- `CONSIDERED_TIME_FRAME:` The time interval over which market data is considered (e.g., "1h", "4h", "1d"). This timeframe is used for technical indicators.  
  `CONSIDERED_TIME_FRAME = "4h"`  # Set to 4 hours by default.
  
- `TRADE_TEST_MODE:` When set to True, the bot operates in test mode, executing trades regardless of whether all test conditions are met.  
  `TRADE_TEST_MODE = False`  # Set to True for testing purposes.
  
- `LIVE_TRADING:` When set to True, the bot executes live trades using real money. Use this mode with caution; ensure that all risk management conditions are properly set before switching to this mode.  
  `LIVE_TRADING = False`  # Set to True for live trading.
  
- `LIVE_TEST_TRADING:` When set to True, the bot will execute real Binance trades but using the `create_test_order()` method. This simulates live trading behavior without risking actual capital, making it ideal for debugging.  
  `LIVE_TEST_TRADING = True`  # Set to True for safe testing of live trades.
  
- `BUY_TRADE_ALLOCATION_PERCENT:` The percentage of your available balance allocated for each buy trade. This controls how much of your balance is used when executing a buy order.  
  `BUY_TRADE_ALLOCATION_PERCENT = 100`  # Default is 100%, meaning all available funds are used for each buy trade.
  
- `SELL_TRADE_ALLOCATION_PERCENT:` The percentage of your available balance allocated for each sell trade. This controls how much of your balance is used when executing a sell order.  
  `SELL_TRADE_ALLOCATION_PERCENT = 100`  # Default is 100%, meaning all available funds are used for each sell trade.

Make sure to create a `.env` file in the root directory of your project and populate it with the above configurations before running the bot.

## Backtesting

The `backtests.py` file is used to backtest your strategies with collected market data.

- Queue multiple bots for sequential execution, excluding data collection bots from backtesting.
- Resumes from the last trading position, allowing for efficient testing and continuity.

## Example Usage

To start the trading bot after configuring your settings, simply execute:

```bash
python main.py
```
## Conclusion

This trading bot framework empowers developers to build and test their trading strategies efficiently. Dive into the code and customize it to meet your trading needs!

## Contribution Guidelines

Contributions to this project are welcome! If you wish to contribute, please fork the repository and submit a pull request. For bug reports or feature requests, use the issue tracker.

## Contact Information

For questions or feedback, please reach out to OpenSourceTradingBot@gmail.com or create an issue in the repository.

&copy; 2024
