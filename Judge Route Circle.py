"""

"""
class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        u = 0
        d = 0
        l = 0
        r = 0
        for move in moves:
            if move == 'U':
                u += 1
            if move == 'D':
                d += 1
            if move == 'L':
                l += 1
            if move == 'R':
                r += 1
        if u == d and l == r:
            return True
        return False


    def judgeCircle_optimized(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        if not moves:
            return True

        if moves.count('U') == moves.count('D') and moves.count('L') == moves.count('R'):
            return True
        else:
            return False

sol = Solution()
print(sol.judgeCircle("UDLR"))