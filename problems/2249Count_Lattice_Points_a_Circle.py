from functools import reduce
import numpy as np
class Solution(object):
    def lattice_points_circle(self, x0, y0, radius):
        x_ = np.arange(x0 - radius - 1, x0 + radius + 1, dtype=int)
        y_ = np.arange(y0 - radius - 1, y0 + radius + 1, dtype=int)
        x, y = np.where((x_[:,np.newaxis] - x0)**2 + (y_ - y0)**2 <= radius**2)
        return {(x, y) for x, y in zip(x_[x], y_[y])}
    
    def countLatticePoints(self, circles):
        """
        :type circles: List[List[int]]
        :rtype: int
        """
        circles = set(tuple(i) for i in circles)
        return len(reduce(lambda x, y: x|y, (self.lattice_points_circle(*i) for i in circles)))