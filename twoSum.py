class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums), 1):
                if nums[i] + nums[j] == target:
                    return [i, j]
                
if __name__ == "__main__":
    sol = Solution()
    # print(sol.twoSum([2,7,11,15],9))
    print(sol.twoSum([3,2,4],6))