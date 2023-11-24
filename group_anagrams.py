class Solution:
    @staticmethod
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

    @staticmethod
    def groupAnagrams(strs):
        final_list = []
        for str1 in strs:
            lst = [str1]
            for str2 in strs:
                if str1 != str2 and Solution.is_anagram(str1, str2):
                    lst.append(str2)
                    strs.remove(str2)
            final_list.append(lst)
        print(final_list)

# Example usage:
Solution.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
