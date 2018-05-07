class Solution:
    def twoSum_brute_force(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

# # Brute force solution

        for i in range(len(nums) - 1):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]


    def twoSum_sorted(self, nums, target):
        # Sort the array
        nums.sort()
        low = 0
        high = len(nums) - 1
        # Reduce possible candidates by removing numbers higher than the target
        # while nums[high] > target:
        #     high -= 1
        # # Eliminate lower values which cannot contriute to solution
        # while nums[high] + nums[low] < target:
        #     low += 1
        # # Find solution in this restricted space
        while True:
            if nums[low] + nums[high] > target:
                high -= 1
            if nums[low] + nums[high] < target:
                low += 1
            if nums[low] + nums[high] == target:
                return [low, high]

    def twoSum_hash_table(self,nums, target):
        # Hash table two pass
        my_dict = {}
        for idx, num in enumerate(nums):
            my_dict[num] = idx
        for idx, num in enumerate(nums):
            complement = target - num
            if complement in my_dict and my_dict[complement] != idx:
                return [idx, my_dict[complement]]