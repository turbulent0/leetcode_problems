
# !!! find from what resulat depends, in this task - depends from prev odd, prev even, and current odd, current even
# because of parities of current and previous: even-even, even-odd, odd-even, odd-odd
def maxScore( nums: list[int], x: int) -> int:
    last_sum_even = -1*float('inf')
    last_sum_odd = -1*float('inf')
    n = len(nums)
    evens, odds = [], []
    if nums[0] % 2==0:
        last_sum_even = nums[0]
        evens.append(nums[0])
    else:
        last_sum_odd = nums[0]
        odds.append(nums[0])
    for i in range(1, n):
        c=nums[i]
        if nums[i] % 2==0:
            last_sum_even = max(last_sum_even+nums[i], last_sum_odd+nums[i]-x)
            evens.append(nums[i])
        else:
            last_sum_odd = max(last_sum_odd+nums[i], last_sum_even+nums[i]-x)
            odds.append(nums[i])
    return max(last_sum_even, last_sum_odd)

# def maxScore2( nums, x):
#     dp = [0, 0]
#     dp[nums[0] & 1] = nums[0]
#     dp[(nums[0] & 1) ^ 1] = float('-inf')
    
#     for i in range(1, len(nums)):
#         dp[nums[i] & 1] = max(dp[nums[i] & 1] + nums[i], dp[(nums[i] & 1) ^ 1] + nums[i] - x)
    
#     return max(dp[0], dp[1])




nums = [2,130, 25, 33]
x = 5
print(maxScore(nums, x))