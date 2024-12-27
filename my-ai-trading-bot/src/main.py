"""
Main entry point for the AI trading bot.
Run: python main.py
"""

import os
import time
import pandas as pd

from solana_integration import SolanaClient
from trading_logic import evaluate_signal, execute_trade


def main():
    print("Starting AI Trading Bot...")

    # Initialize Solana client
    solana_client = SolanaClient()

    # Optionally load existing training data
    data_file_path = os.path.join("training_data", "history.csv")
    if os.path.exists(data_file_path):
        df = pd.read_csv(data_file_path)
        print(f"Loaded training data with {len(df)} records.")
    else:
        print("No existing data found, starting fresh.")

    # Main loop
    while True:
        try:
            # Fetch market data from Solana
            market_data = solana_client.fetch_market_data("TOKEN_MINT_ADDRESS")

            # Evaluate action (buy, sell, or hold)
            action = evaluate_signal(market_data)

            # Execute trade on Solana if needed
            if action in ["BUY", "SELL"]:
                receipt = execute_trade(solana_client, action, quantity=10)
                print("Trade executed:", receipt)
            else:
                print("No trade required this cycle.")

            # Sleep or wait between market checks
            time.sleep(10)  # Adjust to your desired frequency

        except KeyboardInterrupt:
            print("Shutting down bot...")
            break
        except Exception as e:
            print(f"Error in main loop: {e}")
            time.sleep(5)


if __name__ == "__main__":
    main() 