# Title: First Failing Nightly Build
# Difficulty: Easy
# Scenario: A software team runs an automated test suite on each of n consecutive nightly builds. Once a bug
# is introduced, every later build also fails. The results are stored as a list: 0 for a passing build and 1 for a
# failing build. Re-running the full suite for every build is expensive, so the team wants to locate the first failing
# build with as few look-ups as possible.
# Problem statement: The array has the form 0...0 1...1: some number (possibly zero) of 0s followed by 1s.
# Print the 1-based number of the first build with value 1, or -1 if every build passed. Use binary search.
# Input format:
# Line 1: integer n, the number of builds.
# Line 2: n integers (0 or 1), non-decreasing, the test results in build order.
# Output format:
# Print one integer: the 1-based number of the first failing build, or -1.
# Constraints:
# • 1 ≤ n ≤ 10^5
# • Each value is 0 or 1 and the sequence is non-decreasing
# Sample input:
# 10
# 0 0 0 0 0 0 1 1 1 1
# Sample output:
# 7


n = int(input())
arr = list(map(int, input().split()))

low = 0
high = n - 1
answer = -1

while low <= high:
    mid = low + (high - low) // 2

    if arr[mid] == 1:
        answer = mid + 1
        high = mid - 1

    else:
        low = mid + 1

print(answer)