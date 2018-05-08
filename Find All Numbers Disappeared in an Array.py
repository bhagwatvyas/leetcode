"""
Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements of [1, n] inclusive that do not appear in this array.

Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.

Example:

Input:
[4,3,2,7,8,2,3,1]

Output:
[5,6]
"""


class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = []
        set_nums = set(nums)
        for i in range(1, len(nums) + 1):
            if i not in set_nums:
                result.append(i)
        return result

    def findDisappearedNumbers_optimized(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        """

        [-4, -3, -2, -7, 8, 2, -3, -1]
                                             ^
        """

        for x in nums:
            if nums[abs(x) - 1] > 0:
                nums[abs(x) - 1] *= -1

        ans = []

        for i in range(len(nums)):
            if nums[i] > 0:
                ans.append(i + 1)
        return ans



sol = Solution()
print(sol.findDisappearedNumbers([4,3,2,7,8,2,3,1]))