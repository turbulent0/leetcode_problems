# You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

# Return the max sliding window

# #Solution:
# 1) delete first element if it out of the window(index < i-(k+1))
# 2) delete all values, while  nums[i] > deque[-1]
# 3) deque
from collections import deque
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        res = []
        dq = deque()  # store index
        for i in range(len(nums)):
            if dq and dq[0]<i-k+1:  # out of the window
                dq.popleft()
            while dq and nums[dq[-1]]<nums[i]:  # remove impossible candidate
                dq.pop()
            dq.append(i)
            if i>k-2:
                res.append(nums[dq[0]])
        return res