
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