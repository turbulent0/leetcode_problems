
nums1 = [1]
nums2 = []
def median(nums1, nums2):
    n = len(nums1) + len(nums2)
    res = []
    while len(res) < n//2 + 1:
        if nums1 and nums2 and nums1[0] < nums2[0]:
            res.append(nums1.pop(0))
        elif nums2 and nums1 and nums1[0] >= nums2[0]:
            res.append(nums2.pop(0))
        elif nums2 and not nums1:
            res.append(nums2.pop(0))
        elif nums1 and not nums2:
            res.append(nums1.pop(0))
    print(res)
    if n%2 == 0:
        return (res[-1] + res[-2])/2
    else:
        return res[-1]
        
    

# %%
median(nums1, nums2)

# %%



