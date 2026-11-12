# Title: Zero-Balance Triplets
# Difficulty: Medium
# Scenario: An auditor has a list of n ledger adjustments (positive for credits, negative for debits). She
# suspects fraud when three adjustments cancel exactly. She wants every distinct combination of three
# adjustments, taken from three different positions, that adds up to zero, without listing the same combination
# of values twice.
# Problem statement: Given n integers, print all distinct triplets (x, y, z) with x ≤ y ≤ z and x + y + z = 0, where
# the three values come from three different positions. Triplets are distinct as value combinations (for example
# -1 0 1 is listed once even if -1 occurs twice). Print the triplets in lexicographic order, one per line as 'x y z'; if
# there are none print None. Use your own sort.
# Input format:
# Line 1: integer n.
# Line 2: n integers.
# Output format:
# One triplet per line in lexicographic order, or None.
# Constraints:
# • 3 ≤ n ≤ 3000
# • -10^5 ≤ value ≤ 10^5
# Sample input:
# 8
# -1 0 1 2 -1 -4 3 -2
# Sample output:
# -4 1 3
# -2 -1 3
# -2 0 2
# -1 -1 2
# -1 0 1

n = int(input())
arr = list(map(int, input().split()))

# Own iterative merge sort
temp = [0] * n
width = 1

while width < n:
    start = 0

    while start < n:
        mid = start + width
        end = start + 2 * width

        if mid > n:
            mid = n

        if end > n:
            end = n

        i = start
        j = mid
        k = start

        while i < mid and j < end:
            if arr[i] <= arr[j]:
                temp[k] = arr[i]
                i += 1
            else:
                temp[k] = arr[j]
                j += 1
            k += 1

        while i < mid:
            temp[k] = arr[i]
            i += 1
            k += 1

        while j < end:
            temp[k] = arr[j]
            j += 1
            k += 1

        start += 2 * width

    i = 0
    while i < n:
        arr[i] = temp[i]
        i += 1

    width *= 2

# Find unique zero-sum triplets
found = False
i = 0

while i < n - 2:

    if i > 0 and arr[i] == arr[i - 1]:
        i += 1
        continue

    left = i + 1
    right = n - 1

    while left < right:
        total = arr[i] + arr[left] + arr[right]

        if total == 0:
            print(arr[i], arr[left], arr[right])
            found = True

            left_value = arr[left]
            right_value = arr[right]

            while left < right and arr[left] == left_value:
                left += 1

            while left < right and arr[right] == right_value:
                right -= 1

        elif total < 0:
            left += 1
        else:
            right -= 1

    i += 1

if not found:
    print("None")