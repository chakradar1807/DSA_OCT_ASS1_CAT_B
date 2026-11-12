# Title: One-Trade Stock Profit
# Difficulty: Easy
# Scenario: A trader has the closing price of a stock for each of n consecutive days. She may buy one share
# on some day and sell it on a strictly later day (at most one trade). She wants the maximum profit she could
# have made, or 0 if no profitable trade existed.
# Problem statement: Given the daily prices, print the maximum value of price[j] − price[i] over all pairs i < j. If
# that maximum is negative (prices only fall) or n = 1, print 0 (no trade is made). Do not use built-in max or min.
# Input format:
# Line 1: integer n.
# Line 2: n integers, the daily closing prices.
# Output format:
# Print one integer: the maximum profit (0 if none).
# Constraints:
# • 1 ≤ n ≤ 10^5
# • 1 ≤ price ≤ 10^9
# Sample input:
# 8
# 120 98 105 90 112 130 95 118
# Sample output:
# 40

n = int(input())
prices = list(map(int, input().split()))

lowest_price = prices[0]
best_profit = 0

i = 1

while i < n:
    profit = prices[i] - lowest_price

    if profit > best_profit:
        best_profit = profit

    if prices[i] < lowest_price:
        lowest_price = prices[i]

    i += 1

print(best_profit)