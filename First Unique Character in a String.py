"""
Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
Note: You may assume the string contain only lowercase letters.
"""

from sys import maxsize


class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        mydict = {}
        # Populate Dictionary with unique chars
        for idx, char in enumerate(s):
            if char not in mydict:
                mydict[char] = [idx]
            else:
                mydict[char] += [idx]
        # Iterate through dictionary to find char with least index
        solution = maxsize
        found_flag = False
        for char, indexes in mydict.items():
            if len(indexes) == 1 and indexes[0] < solution:
                found_flag = True
                solution = indexes[0]
        return solution if found_flag is True else -1


sol = Solution()
print(sol.firstUniqChar("loveleetcode"))
