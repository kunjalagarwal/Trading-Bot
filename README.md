# Binance Futures Testnet Trading Bot

## Setup

1. Clone repo
2. Install dependencies:
   pip install -r requirements.txt

3. Add .env file:
   API_KEY=your_key
   API_SECRET=your_secret

## Run

Market Order:
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001

Limit Order:
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 60000

## Features
- MARKET and LIMIT orders
- CLI input validation
- Logging to trading.log
- Error handling

## Assumptions
- Binance Futures Testnet account is active
- API keys are valid