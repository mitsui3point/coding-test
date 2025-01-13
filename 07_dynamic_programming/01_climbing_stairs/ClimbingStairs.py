class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        table = {1:1, 2:2}
        def climb(e):
            if e in table:
                return table[e]
            return climb(e - 2) + climb(e - 1)

        return climb(n)

sol = Solution()
print(sol.climbStairs(4))



