# Title: Leaderboard Disorder Count
# Difficulty: Medium
# Scenario: A game server lists players' scores in the order the players finished their matches. A perfectly 'fair'
# queue would have scores in non-decreasing order. To measure unfairness, the analyst counts the number of
# pairs of players where the earlier finisher has a strictly higher score than the later finisher.
# Problem statement: Given n scores in finishing order, count the pairs of positions (i, j) with i < j and score[i]
# > score[j]. Print the count. Equal scores do not form an inversion. Built-in sorting is not allowed. The answer
# can be large, so an O(n2) pair check will not be fast enough for the largest inputs.
# Input format:
# Line 1: integer n.
# Line 2: n space-separated integers, the scores.
# Output format:
# Print one integer: the number of inversions.
# Constraints:
# • 1 ≤ n ≤ 10^5
# • 0 ≤ score ≤ 10^9
# Sample input:
# 6
# 5 3 8 6 2 7
# Sample output:
# 7

def merge_sort(arr, temp, left, right):
    if left >= right:
        return 0

    mid = (left + right) // 2

    count = merge_sort(arr, temp, left, mid)
    count += merge_sort(arr, temp, mid + 1, right)

    i = left
    j = mid + 1
    k = left

    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            temp[k] = arr[i]
            i += 1
        else:
            temp[k] = arr[j]
            count += mid - i + 1
            j += 1

        k += 1

    while i <= mid:
        temp[k] = arr[i]
        i += 1
        k += 1

    while j <= right:
        temp[k] = arr[j]
        j += 1
        k += 1

    for i in range(left, right + 1):
        arr[i] = temp[i]

    return count


n = int(input().strip())
scores = list(map(int, input().strip().split()))

temp = [0] * n

answer = merge_sort(scores, temp, 0, n - 1)

print(answer)