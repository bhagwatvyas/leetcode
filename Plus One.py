"""
Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

Example 1:

Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Example 2:

Input: [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
"""

class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """

        # Edge case to handle here is if last digit is 9. If not, add 1 to last digit and return
        if digits[-1] != 9:
            digits[-1] += 1
            return digits

        # While the last digit is 9, keep making the digit in the list 0, then add the carry at the right place
        i = 1
        while i <= len(digits) and digits[-i] == 9:
            digits[-i] = 0
            i += 1
        # Case when all the digits are 9 (99,999,etc)
        if i == len(digits) + 1:
            # Append 1 to the start of the list
            digits = [1] + digits
        # Add carry to the correct index
        else:
            digits[-i] += 1
        return digits


sol = Solution()
print(sol.plusOne([9,9,8]))