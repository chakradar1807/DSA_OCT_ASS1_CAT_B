# Title: Product Popularity Ordering
# Difficulty: Medium
# Scenario: An online store logs the product ID of every sale. A 'rarity report' lists the sales so that the least
# frequently sold products come first. Products sold equally often are listed with the larger product ID first.
# Each sale is listed individually, so a product sold three times appears three times in a row.
# Problem statement: Given the n product IDs of the sales, output all n IDs arranged so that (1) IDs with
# smaller total frequency come first, and (2) among IDs with the same frequency, the larger ID comes first. All
# copies of one ID are consecutive. Built-in sorting, Counter and sorted() with a key are not allowed; write your
# own sorting routine with a custom comparison.
# Input format:
# Line 1: integer n.
# Line 2: n space-separated integers, the product IDs.
# Output format:
# Print the n IDs in the required order on one line, separated by spaces.
# Constraints:
# • 1 ≤ n ≤ 10^5
# • 1 ≤ ID ≤ 10^9
# Sample input:
# 9
# 4 4 6 2 2 2 6 9 6
# Sample output:
# 9 4 4 6 6 6 2 2 2

n = int(input())
arr = list(map(int, input().split()))

frequency = {}

for value in arr:
    if value in frequency:
        frequency[value] += 1
    else:
        frequency[value] = 1

ids = list(frequency.keys())
u = len(ids)

source = ids
destination = ids[:]

width = 1

while width < u:
    start = 0

    while start < u:
        mid = start + width
        end = start + 2 * width

        if mid > u:
            mid = u

        if end > u:
            end = u

        i = start
        j = mid
        k = start

        while i < mid and j < end:
            a = source[i]
            b = source[j]

            if frequency[a] < frequency[b]:
                destination[k] = a
                i += 1

            elif frequency[a] > frequency[b]:
                destination[k] = b
                j += 1

            elif a > b:
                destination[k] = a
                i += 1

            else:
                destination[k] = b
                j += 1

            k += 1

        while i < mid:
            destination[k] = source[i]
            i += 1
            k += 1

        while j < end:
            destination[k] = source[j]
            j += 1
            k += 1

        start += 2 * width

    source, destination = destination, source
    width *= 2

result = [0] * n
position = 0

for value in source:
    count = frequency[value]

    for j in range(count):
        result[position] = value
        position += 1

print(*result)