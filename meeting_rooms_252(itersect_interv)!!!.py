class Solution:

    
    def canAttendMeetings(self, intervals: list[list[int]]) -> bool:
        if intervals == []:
            return True
        sorted_intervals = sorted(intervals, key= lambda x: x[0]) # !!! need to sort
        flat = [ j for i in sorted_intervals for j in i]
        return flat == sorted(flat)
    
        # # vector operation
        # intervals = np.array(intervals, dtype=int)
        # intervals = intervals[intervals[:, 0].argsort()]
        # return all(intervals[1:, 0] >= np.roll(intervals[:, 1], 1)[1:])