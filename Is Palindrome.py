"""
Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

Example 1:

Input: 121
Output: true

Example 2:
Input: -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:
Input: 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

Follow up:
Coud you solve it without converting the integer to a string?
"""

class Solution:
    def isPalindrome_str(self,x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        rev = str(x)
        print(rev[::-1])
        if x == int(rev[::-1]):
            return True
        return False


    # Without converting integer to string
    def isPalindrome(self,x):
        if x < 0:
            return False

<<<<<<< HEAD
        num = x
        rev = 0
        power = 0
        # determine the power of the number
        while num > 0:
            num = num // 10
            power += 1
        power -= 1

        # reverse the integer and check with original number
        num = x
        while num > 0:
            digit = num % 10
            num = num // 10
            rev += digit * pow(10, power)
            power -= 1

        if rev == x:
            return True
        return False


sol = Solution()
print(sol.isPalindrome(121))
=======

print(isPalindrome(12321))
>>>>>>> 93d486b5e13f077519eba901b5c8b7f639f873a4

