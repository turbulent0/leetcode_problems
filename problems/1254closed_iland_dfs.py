# The DFS function takes a position (i, j) and recursively checks its neighboring cells. If the cell is out of bounds or has a value of 1, it returns True. Otherwise, it marks the cell as visited and continues to recursively check its neighbors. If any of the neighboring cells are not closed islands (i.e., not completely surrounded by 1s), it returns False. If all neighbors are closed islands, it returns True.

# The main function iterates through each cell in the grid and checks if it is a 0 and a closed island. If it is, it increments the count.

# ! islands - 1, water = 0
from typing import List
class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        count = 0
        
        def dfs(i, j):
            if i < 0 or j < 0 or i >= rows or j >= cols or grid[i][j] == 0:
                return True
            grid[i][j] = 0 # mark as visited
            left = dfs(i, j-1)
            right = dfs(i, j+1)
            up = dfs(i-1, j)
            down = dfs(i+1, j)
            return left and right and up and down
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1 and dfs(i, j):
                    count += 1
        
        return count

grid = [[1,1,1,1,1,1,1,0],
        [1,0,0,0,0,1,1,0],
        [1,0,1,0,1,1,1,0],
        [1,0,0,0,0,1,0,1],
        [1,1,1,1,1,1,1,0]]

# grid=   [[0,1,0],
#         [0,0,0],
#         [0,1,1]]
res = Solution()
print(res.closedIsland(grid))