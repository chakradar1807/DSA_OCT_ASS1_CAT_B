# Title: Voice Assistant Vowel Swap
# Difficulty: Easy
# Scenario: A speech-to-text test tool deliberately garbles a phrase to test a spelling-correction feature: it
# keeps every consonant and space where it is, but reverses the order in which the vowels appear along the
# phrase.
# Problem statement: Given a phrase made of English letters and single spaces, reverse the order of its
# vowels (a, e, i, o, u in either case) while all other characters stay in their original positions. Print the resulting
# phrase. Vowel letters keep their own case; only their positions change.
# Input format:
# A single line containing the phrase (letters and spaces; no leading or trailing spaces).
# Output format:
# Print the transformed phrase on one line.
# Constraints:
# • 1 ≤ length ≤ 2 × 10^5
# • Characters are English letters or spaces
# Sample input:
# Campus Library
# Sample output:
# Campis Lubrary


# Approach: Use two pointers to find vowels from both ends.
# Swap the vowels while keeping all other characters in place.
# Time Complexity: O(n)
# Auxiliary Space Complexity: O(n)

phrase = input()
letters = list(phrase)

vowels = "aeiouAEIOU"

left = 0
right = len(letters) - 1

while left < right:

    if letters[left] not in vowels:
        left += 1

    elif letters[right] not in vowels:
        right -= 1

    else:
        temp = letters[left]
        letters[left] = letters[right]
        letters[right] = temp

        left += 1
        right -= 1

for ch in letters:
    print(ch, end="")

print()