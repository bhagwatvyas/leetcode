"""
Given two lists Aand B, and B is an anagram of A. B is an anagram of A means B is made by randomizing the order of the elements in A.

We want to find an index mapping P, from A to B. A mapping P[i] = j means the ith element in A appears in B at index j.

These lists A and B may contain duplicates. If there are multiple answers, output any of them.

For example, given

A = [12, 28, 46, 32, 50]
B = [50, 12, 32, 46, 28]
We should return
[1, 4, 3, 2, 0]
as P[0] = 1 because the 0th element of A appears at B[1], and P[1] = 4 because the 1st element of A appears at B[4], and so on.
Note:

A, B have equal lengths in range [1, 100].
A[i], B[i] are integers in range [0, 10^5].

"""

from collections import defaultdict
class Solution(object):
    def anagramMappings_bruteForce(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        P = []
        i = 0
        while i < len(A):
            j = 0
            while j < len(B):
                if A[i] == B[j]:
                    P.append(j)
                    B[j] = -1
                j += 1
            i += 1
        return P


    def anagramMappings(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        if len(A) != len(B): return []
        mapper = defaultdict(list)
        result = []
        for index, letter in enumerate(B):
            mapper[letter].append(index)

        for letter in A:
            result.append(mapper[letter].pop())

        return result


sol = Solution()
print(sol.anagramMappings_optimized([12, 28, 46, 32, 50], [50, 12, 32, 46, 28]))