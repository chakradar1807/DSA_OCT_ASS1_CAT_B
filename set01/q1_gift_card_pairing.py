# Title: Gift Card Pairing at Checkout
# Difficulty: Easy
# Scenario: An online store lets customers pay with a gift card whose balance must be used up exactly. At
# checkout, the system must find two different items in the customer's cart whose prices add up to exactly the
# gift-card balance.
# Problem statement: Given the prices of the n items in a cart (in the order they were added) and the gift-card
# balance T, find two different positions i and j (0-based, i < j) such that price[i] + price[j] = T. The input
# guarantees that exactly one such pair of positions exists. The same position cannot be used twice.
# Input format:
# Line 1: integer n, the number of items.
# Line 2: n space-separated integers, the item prices.
# Line 3: integer T, the gift-card balance.
# Output format:
# Print two space-separated integers i and j (0-based, i < j) on one line.
# Constraints:
# • 2 ≤ n ≤ 10^5
# • 1 ≤ price[i] ≤ 10^9
# • 1 ≤ T ≤ 2 × 10^9
# • Exactly one pair of positions (i, j) satisfies the condition
# Sample input:
# 6
# 120 45 80 200 35 150
# 235
# Sample output:
# 3 4

n = int(input().strip())
prices = list(map(int, input().split()))
target = int(input().strip())

seen = {}

for j in range(n):
    needed = target - prices[j]

    if needed in seen:
        print(seen[needed], j)
        break

    if prices[j] not in seen:
        seen[prices[j]] = j