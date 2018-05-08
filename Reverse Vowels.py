"""
Write a function that takes a string as input and reverse only the vowels of a string.

Example 1:
Given s = "hello", return "holle".

Example 2:
Given s = "leetcode", return "leotcede".

Note:
The vowels does not include the letter "y".

"""


class Solution:
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        # Since strings are immutable in Python, convert string to list
        s_list = list(s)
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        # Store vowel indices in list
        indexes = []
        for idx, char in enumerate(s_list):
            if char in vowels:
                indexes.append(idx)
        low = 0
        high = len(indexes) - 1

        while low < high:
            s_list[indexes[low]], s_list[indexes[high]] = s_list[indexes[high]], s_list[indexes[low]]
            low += 1
            high -= 1

        return ''.join(x for x in s_list)


    def reverseVowels_optimized(self,s):
        # Since strings are immutable in Python, convert string to list
        s_list = list(s)
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

        low = 0
        high = len(s_list) - 1

        while low < high:
            while s_list[low] not in vowels and low < high:
                low += 1
            while s_list[high] not in vowels and low < high:
                high -= 1
            s_list[low], s_list[high] = s_list[high], s_list[low]
            low += 1
            high -= 1

        return ''.join(x for x in s_list)


sol = Solution()
print(sol.reverseVowels("leetcode"))