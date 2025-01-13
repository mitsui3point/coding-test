class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        visited = {}

        def dfs(cur_v):
            visited[cur_v] = True
            for next_v in rooms[cur_v]:
                if next_v not in visited:
                    dfs(next_v)

        dfs(0)
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
result = sol.canVisitAllRooms(rooms2)
print(f"result:{result}")
