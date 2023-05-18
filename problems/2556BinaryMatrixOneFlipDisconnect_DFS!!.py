# 2 times DFS with filling 0- then at least two different paths and matrix can not be disconnected

class Solution(object):
    def dfs(self, grid, i, j):
        if i+1 == len(grid) and j+1 == len(grid[0]):
            return True
        if i >= len(grid) or j >= len(grid[0]) or grid[i][j] == 0:
            return False
        grid[i][j] = 0
        return self.dfs(grid, i+1, j) or self.dfs(grid, i, j+1)

    def isPossibleToCutPath(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: bool
        """
        if self.dfs(grid, 0, 0):
            grid[0][0] = 1
            return not self.dfs(grid, 0, 0)
        return True