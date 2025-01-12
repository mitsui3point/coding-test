from collections import deque


class Solution(object):
    def shortestPathBinaryMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        d_row = [1, -1, 1]
        d_col = [1, 0, -1]
        max_row = len(grid)
        max_col = len(grid[0])
        visited = []
        results = []
        # init = (0, 0)
        init = (0, 0)
        row, col = init

        def bfs(current):
            # n = len(grid)
            queue = deque()
            queue.append(current)
            visited.append(current)
            while queue:
                row, col = queue.popleft()
                # TODO: index out of range 핸들링
                for i in range(3):
                    row = row + d_row[i]
                    col = col + d_col[i]
                    print(f"i:{i} row:{row}, col:{col}, queue:{queue}, visited:{visited}")
                    if (
                        (0 <= row < max_row and 0 <= col < max_col)
                        and (grid[row][col] == 0)
                        and ((row, col) not in visited)
                    ):
                        queue.append((row, col))
                        visited.append((row, col))
                        if (i == 0):  # dx dy i == 0 일경우 : cross 이므로 최단경로이기 때문에 for loop exit
                            break
        if grid[row][col] == 0:
            bfs(init)
        if len(visited) > 0:
            return len(visited)
        return -1
    
    
if __name__ == "__main__":
    sol = Solution()
    grid1 = [[0, 1], [1, 0]]
    grid2 = [[0, 0, 0], [1, 1, 0], [1, 1, 0]]
    grid3 = [[1, 0, 0], [1, 1, 0], [1, 1, 0]]
    print(f"result:{sol.shortestPathBinaryMatrix(grid1)}")
