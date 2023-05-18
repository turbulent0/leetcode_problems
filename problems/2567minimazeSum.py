
# nlog(n), for O(n) take 3 largest and 3 smallest elements
def minimizeSum(nums):
    nums_sorted = sorted(nums[2:-2])  
    print(nums_sorted) 
    if len(nums_sorted) >= 4:
        return min(max(nums_sorted[-1], nums[1], nums[-2]) - min(nums_sorted[0], nums[1], nums[-2]), 
                   max(nums_sorted[-1], nums[0], nums[1]) - min(nums_sorted[0], nums[0], nums[1]),
                   max(nums_sorted[-1], nums[-2], nums[-1]) - min(nums_sorted[0], nums[-2], nums[-1])
                   )
    # Return the minimum score
    return  0