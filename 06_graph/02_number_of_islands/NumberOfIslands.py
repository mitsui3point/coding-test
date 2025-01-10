from collections import deque


class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        results = []
        visited = []
        max_x = len(grid[0]) - 1
        max_y = len(grid) - 1
        # right, down, left, up
        dx = [0, 1, -1, -1, 1]
        dy = [0, 0, 1, -1, -1]

        def bfs(v):
            q = deque()
            q.append(v)
            while q:
                cur_y, cur_x = q.popleft()
                for i in range(5):
                    cur_x = cur_x + dx[i]
                    cur_y = cur_y + dy[i]
                    if (
                        (0 <= cur_x <= max_x and 0 <= cur_y <= max_y)
                        and ((cur_y, cur_x) not in visited)
                        and (grid[cur_y][cur_x] == "1")
                    ):
                        q.append((cur_y, cur_x))
                        visited.append((cur_y, cur_x))

        for y in range(len(grid)):
            for x in range(len(grid[y])):
                if grid[y][x] == "1":
                    bfs((y, x))
                    result = [x for x in visited] # list comprehension(리스트 컴프리핸션); 리스트 깊은 복사를 위해
                    if result not in results:
                        results.append(result)
        return len(results)


if __name__ == "__main__":
    grid = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"],
        # ["1", "1", "0", "0", "0"],
        # ["1", "1", "0", "0", "0"],
        # ["0", "0", "1", "0", "0"],
        # ["0", "0", "0", "1", "1"],
        # ["1", "1", "0"],
        # ["1", "1", "0"],
        # ["0", "0", "0"],
    ]
    solution = Solution()
    print(solution.numIslands(grid))
