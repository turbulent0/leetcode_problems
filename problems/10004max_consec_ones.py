class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = right = zeros = max1 = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                zeros += 1
            while zeros > k:
                if nums[left] == 0:
                    zeros -= 1
                left += 1
            max1 = max(max1, right - left + 1)
            right += 1
        return max1
    
    # def longestOnes(self, A, K):
    #     i = 0
    #     for j in xrange(len(A)):
    #         K -= 1 - A[j]
    #         if K < 0:
    #             K += 1 - A[i]
    #             i += 1
    #     return j - i + 1