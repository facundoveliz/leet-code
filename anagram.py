def is_anagram(s, t):
    if len(s) != len(t):
        return False

    char_count = {}

    # Increment character count for string s
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    # Decrement character count for string t
    for char in t:
        if char in char_count:
            char_count[char] -= 1
        else:
            return False  # If a character in t is not in s, they can't be anagrams

    # Check if all character counts are zero
    for count in char_count.values():
        if count != 0:
            return False

    return True


# Test cases
print(is_anagram("anagram", "nagaram"))  # Output: True
print(is_anagram("rat", "car"))  # Output: False
