
# n**2 solution
import numpy as np
from typing import List
def minMeetingRooms( intervals: List[List[int]]) -> int:
    sorted_intervals = sorted(intervals, key= lambda x: x[0])
    n = len(sorted_intervals)
    comp_matrix = np.zeros((n, n), dtype=int)
    for i in range(n-1):
        for j in range(i+1, n):
            if sorted_intervals[i][1] > sorted_intervals[j][0]:
                comp_matrix[i, j] = 1
    return comp_matrix

# nlogn solution
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        sorted_intervals = sorted(intervals, key= lambda x: x[0])
        heapq = []
        n = len(sorted_intervals)
        heappush(heapq, sorted_intervals[0][1])
        for i in range(1, n):
            if sorted_intervals[i][0] >= heapq[0]:
                heappop(heapq)
            heappush(heapq, sorted_intervals[i][1])
        return len(heapq)
    
 

intervals = [[5,8],[6,8]]
minMeetingRooms(intervals)

