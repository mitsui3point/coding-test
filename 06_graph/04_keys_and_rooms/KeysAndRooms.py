class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        init = rooms[0]
        visited = [False for _ in range(len(rooms))]

        def dfs(room):
            for cur_v in room:
                if init == room:
                    visited[0] = True
                if not visited[cur_v]: 
                    visited[cur_v] = True
                    dfs(rooms[cur_v])

        dfs(init)
        for v in visited:
            if not v:
                return False
        return True


"""
rooms[
    [1], [2]
]
"""
rooms1 = [[1], [2], [3], []]
rooms2 = [[1, 3], [3, 0, 1], [2], [0]]
rooms3 = [[1, 3], [2, 4], [0], [4], [], [3, 4]]
sol = Solution()
result = sol.canVisitAllRooms(rooms1)
print(f"result:{result}")
