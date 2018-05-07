"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:

Input: "()"
Output: true
Example 2:

Input: "()[]{}"
Output: true
Example 3:

Input: "(]"
Output: false
Example 4:

Input: "([)]"
Output: false
Example 5:

Input: "{[]}"
Output: true
"""

class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        mydict = {'(': ')', '[': ']', '{': '}'}
        stack = []
        dictkeys = mydict.keys()
        dictvalues = mydict.values()

        # Handle edge cases
        # An empty string is considered valid
        if s == "":
            return True

        # A string cannot be a valid palindrome if length is odd
        if len(s) % 2 != 0:
            return False

        # Return False if first element is a closing bracket or last element is opening bracket
        if s[0] in dictvalues or s[-1] in dictkeys:
            return False

        for char in s:
            if char in dictkeys:
                stack.append(char)
            elif mydict[stack[-1]] == char:
                stack.pop()
            else:
                return False
        return True





sol = Solution()
print(sol.isValid("([]{})"))