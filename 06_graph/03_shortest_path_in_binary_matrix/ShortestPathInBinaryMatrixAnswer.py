from collections import deque


class Solution(object):
    def shortestPathBinaryMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        init = (0, 0, 1)
        init_r, init_c, init_path = init
        if grid[init_r][init_c] != 0:
            return -1
        
        row = len(grid)
        col = len(grid[0])
        direction = [
            # left right up down
            # lu ld ru rd
            (0, -1), (0, 1), (1, 0), (-1, 0),
            (1, -1), (-1, 1), (1, 1), (-1, -1),
        ]
        queue = deque()
        queue.append(init)
        visited = [[False] * col for _ in range(row)]
        visited[init[0]][init[1]] = False
        print(visited)
        while queue:
            cur_r, cur_c, cur_path = queue.popleft()
            print(f"cur_r:{cur_r}, cur_c:{cur_c}, cur_path:{cur_path}")
            if cur_r >= row - 1 and cur_c >= col - 1:
                result = cur_path
                break
            for dr, dc in direction:
                next_r = cur_r + dr
                next_c = cur_c + dc
                next_path = cur_path + 1
                if (
                    0 <= next_r < row
                    and 0 <= next_c < col
                    and grid[next_r][next_c] == 0
                    and not visited[next_r][next_c]
                ):
                    queue.append((next_r, next_c, next_path))
                    visited[next_r][next_c] = True
        return result


if __name__ == "__main__":
    sol = Solution()
    grid = [
        [0, 0, 0, 1, 0, 0, 0],
        [0, 1, 1, 1, 0, 1, 0],
        [0, 1, 0, 0, 0, 1, 0],
        [0, 0, 0, 1, 1, 1, 0],
        [0, 1, 0, 0, 0, 0, 0],
    ]
    grid1 = [[0, 1], [1, 0]]
    grid2 = [[0, 0, 0], [1, 1, 0], [1, 1, 0]]
    grid3 = [[1, 0, 0], [1, 1, 0], [1, 1, 0]]
    print(f"result:{sol.shortestPathBinaryMatrix(grid)}")
