class Solution:
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 1:
            return True
        if n % 2 != 0:
            return False
        while n > 1.0:
            n = float(n / 2)
            print(n)
        if n != 1:
            return False
        return True

sol = Solution()
print(sol.isPowerOfTwo(126))
