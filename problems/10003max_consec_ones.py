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