# Title: K-th Highest Salary
# Difficulty: Medium
# Scenario: An HR analyst has the monthly salaries of n employees (many people share salaries) and needs
# the k-th highest salary, counting duplicates as separate people, for a benefits-eligibility cut-off. Sorting
# everyone just to read one value is wasteful.
# Problem statement: Given n salaries and an integer k, print the k-th largest element of the multiset: the
# value that would be at position k if the salaries were arranged in non-increasing order (k = 1 is the
# maximum). Duplicates count separately. Built-in sorting is not allowed; use partitioning.
# Input format:
# Line 1: integers n and k.
# Line 2: n space-separated integers, the salaries.
# Output format:
# Print one integer: the k-th largest salary.
# Constraints:
# • 1 ≤ k ≤ n ≤ 10^5
# • 1 ≤ salary ≤ 10^9
# Sample input:
# 9 3
# 40 25 60 25 90 75 60 30 50
# Sample output:
# 60


n, k = map(int, input().strip().split())
salaries = list(map(int, input().strip().split()))

target = n - k

left = 0
right = n - 1

while left <= right:

    middle = (left + right) // 2

    pivot = salaries[middle]

    temp = salaries[middle]
    salaries[middle] = salaries[right]
    salaries[right] = temp

    position = left

    for i in range(left, right):
        if salaries[i] < pivot:
            temp = salaries[i]
            salaries[i] = salaries[position]
            salaries[position] = temp
            position += 1

    temp = salaries[position]
    salaries[position] = salaries[right]
    salaries[right] = temp

    if position == target:
        print(salaries[position])
        break

    elif position < target:
        left = position + 1

    else:
        right = position - 1