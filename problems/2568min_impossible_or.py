
# to solve check first 6 solutions
class Solution(object):
    def minImpossibleOR(self, A):
        """
        :type nums: List[int]
        :rtype: int
        """
        A = set(A)
        return next(1 << i for i in range(31) if (1 << i) not in A)