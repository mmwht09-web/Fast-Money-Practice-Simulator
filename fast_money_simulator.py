import random
import csv
from datetime import datetime

# ==========================================
# FAST MONEY PRACTICE SIMULATOR
# ==========================================

LICENSE = """
FAST MONEY PRACTICE SIMULATOR LICENSE
=====================================

Copyright (c) 2025 Melissa Jené White-Hart

This software is licensed under the Creative Commons
Attribution-NonCommercial-NoDerivatives 4.0 International License (CC-BY-NC-ND 4.0).

You may use this software for personal educational purposes only.
You may NOT:
- Sell, redistribute, or share the files in any form
- Modify or create derivative works
- Use this software for real financial trading

DISCLAIMER:
This software is for educational simulation purposes only.
It does not provide financial, investment, or trading advice.
No real market data is used.
Results do not represent real-world outcomes.
Use at your own risk.
"""

print(LICENSE)

consent = input("Type 'I AGREE' to continue: ")
if consent.strip().upper() != "I AGREE":
    print("Consent not given. Program exited.")
    exit()

starting_balance = 20.0
balance = starting_balance
trade_size = 5.0
take_profit = 0.15
stop_loss = -0.10
trades_per_session = 5

wins = 0
losses = 0
max_balance = balance
max_drawdown = 0
trade_log = []

print(f"\nStarting balance: ${balance:.2f}\n")

for trade in range(1, trades_per_session + 1):
    if balance < trade_size:
        break

    market_move = random.uniform(-0.3, 0.3)
    profit_loss = trade_size * market_move
    outcome = "BREAKEVEN"

    if market_move >= take_profit:
        profit_loss = trade_size * take_profit
        outcome = "WIN"
        wins += 1
    elif market_move <= stop_loss:
        profit_loss = trade_size * stop_loss
        outcome = "LOSS"
        losses += 1

    balance += profit_loss
    max_balance = max(max_balance, balance)
    max_drawdown = max(max_drawdown, max_balance - balance)

    trade_log.append([trade, outcome, round(profit_loss, 2), round(balance, 2)])

    print(f"Trade {trade}: {outcome} | P/L ${profit_loss:.2f} | Balance ${balance:.2f}")

filename = f"session_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
with open(filename, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Trade", "Outcome", "Profit/Loss", "Balance"])
    writer.writerows(trade_log)

print("\nSESSION SUMMARY")
print(f"Ending Balance: ${balance:.2f}")
print(f"Wins: {wins} | Losses: {losses}")
print(f"Max Drawdown: ${max_drawdown:.2f}")
print(f"Session exported to {filename}")
print("Discipline > Speed")