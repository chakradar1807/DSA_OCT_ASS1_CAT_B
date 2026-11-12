# Title: Mirror Coupon Code
# Difficulty: Easy
# Scenario: A shop issues 'mirror coupons': a promotion phrase is valid for the lucky-mirror discount only if it
# reads the same forwards and backwards. Customers type the phrase with spaces, punctuation and mixed
# capitals, and all of these must be ignored when checking.
# Problem statement: Given a line of text, decide whether it is a palindrome after ignoring every character
# that is not a letter or digit and treating uppercase and lowercase letters as equal. Print YES if it is a
# palindrome and NO otherwise. A phrase that contains no letters or digits at all counts as a palindrome.
# Slicing and reversal shortcuts (s[::-1], reversed) are not allowed.
# Input format:
# A single line containing the phrase (letters, digits, spaces and punctuation).
# Output format:
# Print YES or NO.
# Constraints:
# • 1 ≤ length of the line ≤ 2 × 10^5
# • The line contains printable ASCII characters
# Sample input:
# Was it a car or a cat I saw?
# Sample output:
# YES

text = input()

left = 0
right = len(text) - 1

answer = "YES"

while left < right:

    if not text[left].isalnum():
        left += 1

    elif not text[right].isalnum():
        right -= 1

    elif text[left].lower() != text[right].lower():
        answer = "NO"
        break

    else:
        left += 1
        right -= 1

print(answer)