
# we make Sum (take interval) while it is not !negative - the core of algo
def maxSubArray( nums: list[int]) -> int:
    Max = nums[0]
    Sum = 0
    for num in nums:
        Sum += num
        Max = max(Max, Sum)
        if Sum<0:
            Sum = 0
    return Max

nums = [-2,1,-3,4,-1,2,1,-5,4]
print(maxSubArray(nums))

# dp
class Solution:  # 2516 ms, faster than 64.96%
    def lengthOfLIS(self, nums: list[int]) -> int:
        
        n = len(nums)
        dp = [1] * n
        for i in range(n):
            for j in range(i):
                i_=nums[i]
                j_=nums[j]
                if nums[i] > nums[j] and dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
        return max(dp)
res = Solution()
res.lengthOfLIS([1,3,4,2,1,7,2,9,19])