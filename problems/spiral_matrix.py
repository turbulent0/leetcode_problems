matrix = [[1,2,3],[4,5,6],[7,8,9]]
[1,2,3,6,9,8,7,4,5]

# with recursion
def snail(array):
    return list(array[0]) + snail(list(reversed(list(zip(*array[1:]))))) if array else []


matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
print(snail(matrix))

# without recursion

class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        spiralOrder = []
        n, m = len(matrix), len(matrix[0])
        r, c, dr, dc = 0, 0, 0, 1
        while len(spiralOrder) < n * m:
            spiralOrder.append(matrix[r][c])
            matrix[r][c] = float('inf')
            if not(0 <= r + dr < n) or not(0 <= c + dc < m) or matrix[r + dr][c + dc] == float('inf'):
                dr, dc = dc, -dr
            r += dr
            c += dc
        return spiralOrder



