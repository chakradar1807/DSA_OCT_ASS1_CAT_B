# Title: Out-of-Stock Items to the End
# Difficulty: Easy
# Scenario: A warehouse dashboard shows the stock count of n products in catalogue order. Products with
# count 0 are out of stock and should be pushed to the end of the list so that available products appear first,
# but the relative order of the available products must stay exactly as in the catalogue. The dashboard runs on
# a small device, so the rearrangement should happen inside the same array.
# Problem statement: Given n stock counts, move every 0 to the end while keeping the relative order of the
# non-zero counts. Print the rearranged counts. Try to do it in a single pass without creating a second array.
# Input format:
# Line 1: integer n.
# Line 2: n space-separated integers, the stock counts.
# Output format:
# Print the rearranged counts on one line separated by spaces.
# Constraints:
# • 1 ≤ n ≤ 10^5
# • 0 ≤ count ≤ 10^9
# Sample input:
# 9
# 0 14 0 3 7 0 0 9 5
# Sample output:
# 14 3 7 9 5 0 0 0 0


n = int(input())
items = list(map(int, input().split()))

position = 0

for i in range(n):
    if items[i] != 0:
        items[position] = items[i]
        position += 1

while position < n:
    items[position] = 0
    position += 1

for i in range(n):
    if i > 0:
        print(" ", end="")
    print(items[i], end="")

print()