# Title: Longest Unique Scan Run
# Difficulty: Medium
# Scenario: A conveyor belt scanner reads an item code for every parcel passing by. Quality control wants the
# longest stretch of consecutive parcels in which no code appears twice, because such stretches can be
# audited as 'clean' batches.
# Problem statement: Given the sequence of n scanned item codes, print the length of the longest
# contiguous segment in which all codes are different.
# Input format:
# Line 1: integer n.
# Line 2: n space-separated integers, the item codes.
# Output format:
# Print one integer: the length of the longest segment with no repeated code.
# Constraints:
# • 1 ≤ n ≤ 10^5
# • 1 ≤ code ≤ 10^9
# Sample input:
# 10
# 12 7 9 4 5 3 12 6 8 2
# Sample output:
# 9


n = int(input().strip())
codes = list(map(int, input().strip().split()))

last_position = {}

left = 0
longest = 0

for right in range(n):
    value = codes[right]

    if value in last_position:
        if last_position[value] >= left:
            left = last_position[value] + 1

    last_position[value] = right

    current_length = right - left + 1

    if current_length > longest:
        longest = current_length

print(longest)