from collections import deque


class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        init_v = 0
        queue = deque()
        queue.append(init_v)
        visited = {}

        def bfs(cur_v):
            print(f'queue:{queue}, visited:{visited}')
            visited[cur_v] = True
            for next_v in rooms[cur_v]:
                if next_v not in visited:
                    queue.append(next_v)
                    bfs(next_v)

        bfs(init_v)
        print(visited)
        return len(visited) == len(rooms)


"""
rooms[
    [1], [2]
]
"""
rooms1 = [[1], [2], [3], []]
rooms2 = [[1, 3], [3, 0, 1], [2], [0]]
rooms3 = [[1, 3], [2, 4], [0], [4], [], [3, 4]]
sol = Solution()
result = sol.canVisitAllRooms(rooms3)
print(f"result:{result}")
