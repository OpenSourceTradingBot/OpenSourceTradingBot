<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Open Source Trading Bot</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 20px;
            padding: 20px;
            background-color: #f4f4f4;
        }
        h1, h2, h3 {
            color: #333;
        }
        h1 {
            border-bottom: 2px solid #333;
        }
        pre {
            background-color: #eee;
            padding: 10px;
            border-radius: 5px;
            overflow-x: auto;
        }
        code {
            background-color: #eee;
            padding: 2px 4px;
            border-radius: 3px;
        }
        ul {
            list-style-type: square;
        }
        .footer {
            margin-top: 20px;
            font-size: 0.8em;
            color: #666;
        }
    </style>
</head>
    <body>

        <h1>Open Source Trading Bot</h1>

        <h2>Description</h2>
        <p>The Open Source Trading Bot is a robust framework for developers to rapidly create, implement, and backtest custom algorithmic trading strategies. This project provides a clear path for collecting, storing, and analyzing market data, enabling the execution of real-time trades based on defined criteria.</p>

        <h2>Table of Contents</h2>
        <ul>
            <li><a href="#disclaimer">Disclaimer</a></li>
            <li><a href="#key-features">Key Features</a></li>
            <li><a href="#getting-started">Getting Started</a></li>
            <li><a href="#configuration">Configuration</a></li>
            <li><a href="#main-execution-flow">Main Execution Flow</a></li>
            <li><a href="#rsi-example-bot">RSI Example Bot</a></li>
            <li><a href="#rsi-example-bot-configuration">RSI Example Bot Configuration</a></li>
            <li><a href="#backtesting">Backtesting</a></li>
            <li><a href="#example-usage">Example Usage</a></li>
            <li><a href="#conclusion">Conclusion</a></li>
            <li><a href="#contribution-guidelines">Contribution Guidelines</a></li>
            <li><a href="#license-information">License Information</a></li>
            <li><a href="#contact-information">Contact Information</a></li>
        </ul>

        <h2 id="disclaimer">Disclaimer</h2>
        <p>The Open Source Trading Bot is intended for educational and informational purposes only. By using this software, you acknowledge and agree to the following:</p>
        <ul>
            <li><strong>No Financial Responsibility:</strong> The developer(s) of this project are not responsible for any financial losses or damages incurred as a result of using this trading bot or any strategies implemented within it. Trading cryptocurrencies involves substantial risk, and you should only invest what you can afford to lose.</li>
            <li><strong>No Guarantees:</strong> There are no guarantees of profit or success when using this bot. Performance may vary based on market conditions and individual trading strategies.</li>
            <li><strong>Do Your Own Research:</strong> It is essential to conduct thorough research and consider your financial situation and risk tolerance before engaging in any trading activities.</li>
            <li><strong>Third-Party Services:</strong> This bot interacts with third-party services (e.g., Binance API). Any issues or downtime experienced with these services are outside the control of the developer(s) and should be addressed directly with the service provider.</li>
        </ul>
        <p>By proceeding with the use of this bot, you acknowledge that you understand the risks involved and accept full responsibility for your trading activities.</p>

        <h2 id="key-features">Key Features</h2>
        <ul>
            <li>
                <strong>Algorithmic Trading:</strong> Easily implement and customize trading strategies tailored to your preferences. The bot supports various indicators and conditions, allowing you to automate trading decisions based on technical analysis.
            </li>
            <li>
                <strong>Backtesting Capabilities:</strong> Evaluate your strategies against historical market data to refine performance before deploying them live. The backtesting module enables you to simulate trades and analyze results, helping you to optimize parameters and understand potential outcomes.
            </li>
            <li>
                <strong>Python-Friendly:</strong> Designed for developers familiar with Python, offering straightforward modification options. The codebase is modular, making it easy to add new features, strategies, or integrate additional data sources without extensive rewrites.
            </li>
            <li>
                <strong>Data Collection and Management:</strong> The bot includes a robust data collection module that retrieves real-time market data from the Binance API. Historical data is stored in a database for easy access, enabling effective analysis and strategy development.
            </li>
            <li>
                <strong>Customizable Risk Management:</strong> Implement your risk management rules with flexible options for stop-loss and take-profit settings. You can adjust parameters based on market conditions or personal risk tolerance to safeguard your investments.
            </li>
            <li>
                <strong>Multi-Strategy Support:</strong> Run multiple trading strategies simultaneously, allowing for diversified trading approaches. You can queue different bots to manage various assets or strategies, maximizing trading opportunities.
            </li>
            <li>
                <strong>Logging and Monitoring:</strong> Comprehensive logging features capture all bot activities, including trades executed, errors encountered, and market data fetched. This functionality allows for easy troubleshooting and performance monitoring.
            </li>
            <li>
                <strong>Community-Driven:</strong> As an open-source project, the bot encourages contributions from the community. You can share strategies, improvements, and insights with other developers, fostering collaboration and innovation.
            </li>
        </ul>


        <h2 id="getting-started">Getting Started</h2>
        <h3>Installation</h3>
        <p>Clone the repository and install the necessary dependencies.</p>
        <pre><code>git clone https://github.com/OpenSourceTradingBot/OpenSourceTradingBot.git
    cd OpenSourceTradingBot
    pip install -r requirements.txt</code></pre>

        <h3>Database Setup</h3>
        <p>Use Alembic to generate the database tables. Ensure you have a database configured in your alembic.ini file.</p>
        <pre><code>alembic upgrade head</code></pre>

        <h3>Scheduling</h3>
        <p>Set up a scheduler (e.g., cron job or Windows Task Scheduler) to run the bot. The default interval is set to 300 seconds (5 minutes).</p>

        <h2 id="configuration">Configuration</h2>
        <p>To customize the trading bot, you will need to set up a configuration file (e.g., .env) with the following variables:</p>
        <ul>
            <li><code>DATABASE_URL:</code> The connection URL for your database. Replace username, password, ipaddress, and database with your database credentials and information.<br><code>DATABASE_URL="mysql+pymysql://username:password@ipaddress/database"</code></li>
            <li><code>BINANCE_API_KEY:</code> Your Binance API key. Obtain this from your Binance account settings to allow the bot to access your trading account.<br><code>BINANCE_API_KEY="API_KEY"</code></li>
            <li><code>BINANCE_API_SECRET:</code> Your Binance API secret. This is required for secure API access and should be kept confidential.<br><code>BINANCE_API_SECRET="API_SECRET"</code></li>
            <li><code>ITERATION_TIME:</code> The interval (in seconds) at which the bot runs its trading strategy. The default is set to 300 seconds (5 minutes).<br><code>ITERATION_TIME=300</code></li>
            <li><code>EXCEPTION_LOG_FILE_NAME:</code> The filename for logging exceptions that occur during the execution of the bot. This file will help you debug issues.<br><code>EXCEPTION_LOG_FILE_NAME="exception.log"</code></li>
        </ul>

        <h2 id="main-execution-flow">Main Execution Flow</h2>
        <ul>
            <li><strong>main.py:</strong> The core execution file that orchestrates the bot's operations.</li>
            <li><strong>Data Collection:</strong> The binance_data_collector retrieves the latest market data from the Binance API and stores it in the database.</li>
            <li><strong>Strategy Execution:</strong> The RSI_example bot processes the market data, assessing whether to buy or sell based on specified conditions.</li>
        </ul>

        <h2 id="rsi-example-bot">RSI Example Bot</h2>
        <ul>
            <li>Allows for a customizable timeframe (e.g., last 4 weeks) to optimize data usage.</li>
            <li>Analyzes previous trades to determine buy/sell actions.</li>
            <li>Executes orders based on defined tests and updates the trades table accordingly.</li>
        </ul>

        <h2 id="rsi-example-bot-configuration">RSI Example Bot Configuration</h2>
        <p>In addition to the general configuration, you will need to specify settings for the RSI_example bot in your configuration file. Here are the key parameters:</p>
        <ul>
            <li><code>BOT_ID:</code> The unique identifier for this bot instance. It is used to track the bot in the system.<br><code>BOT_ID = 1</code> # Default ID for this bot.</li>
            <li><code>BOT_NAME:</code> The name of the bot, used for logging and identification purposes. You can change this as needed.<br><code>BOT_NAME = "RSI_example"</code></li>
            <li><code>SYMBOL_ID:</code> The unique identifier for the trading symbol (e.g., BTC, ETH, etc.). This should correspond to the asset you're trading.<br><code>SYMBOL_ID = 12</code> # Default symbol ID.</li>
            <li><code>CONSIDERED_TIME_FRAME:</code> The time interval over which market data is considered (e.g., "1h", "4h", "1d"). This timeframe is used for technical indicators.<br><code>CONSIDERED_TIME_FRAME = "4h"</code> # Set to 4 hours by default.</li>
            <li><code>TRADE_TEST_MODE:</code> When set to True, the bot operates in test mode, executing trades regardless of whether all test conditions are met.<br><code>TRADE_TEST_MODE = False</code> # Set to True for testing purposes.</li>
            <li><code>LIVE_TRADING:</code> When set to True, the bot executes live trades using real money. Use this mode with caution; ensure that all risk management conditions are properly set before switching to this mode.<br><code>LIVE_TRADING = False</code> # Set to True for live trading.</li>
            <li><code>LIVE_TEST_TRADING:</code> When set to True, the bot will execute real Binance trades but using the <code>create_test_order()</code> method. This simulates live trading behavior without risking actual capital, making it ideal for debugging.<br><code>LIVE_TEST_TRADING = True</code> # Set to True for safe testing of live trades.</li>
            <li><code>BUY_TRADE_ALLOCATION_PERCENT:</code> The percentage of your available balance allocated for each buy trade. This controls how much of your balance is used when executing a buy order.<br><code>BUY_TRADE_ALLOCATION_PERCENT = 100</code> # Default is 100%, meaning all available funds are used for each buy trade.</li>
            <li><code>SELL_TRADE_ALLOCATION_PERCENT:</code> The percentage of your available balance allocated for each sell trade. This controls how much of your balance is used when executing a sell order.<br><code>SELL_TRADE_ALLOCATION_PERCENT = 100</code> # Default is 100%, meaning all available funds are used for each sell trade.</li>
        </ul>
        <p>Make sure to create a .env file in the root directory of your project and populate it with the above configurations before running the bot.</p>

        <h2 id="backtesting">Backtesting</h2>
        <p>The <code>backtests.py</code> file is used to backtest your strategies with collected market data.</p>
        <ul>
            <li>Queue multiple bots for sequential execution, excluding data collection bots from backtesting.</li>
            <li>Resumes from the last trading position, allowing for efficient testing and continuity.</li>
        </ul>

        <h2 id="example-usage">Example Usage</h2>
        <p>To start the trading bot after configuring your settings, simply execute:</p>
        <pre><code>python main.py</code></pre>

        <h2 id="conclusion">Conclusion</h2>
        <p>This trading bot framework empowers developers to build and test their trading strategies efficiently. Dive into the code and customize it to meet your trading needs!</p>

        <h2 id="contribution-guidelines">Contribution Guidelines</h2>
        <p>Contributions to this project are welcome! If you wish to contribute, please fork the repository and submit a pull request. For bug reports or feature requests, use the issue tracker.</p>

        <h2 id="contact-information">Contact Information</h2>
        <p>For questions or feedback, please reach out to OpenSourceTradingBot@gmail.com or create an issue in the repository.</p>

        <div class="footer">
            <p>&copy; 2024</p>
        </div>

    </body>
</html>