class Solution(object):
    def twoSum(self, nums, target):
        d = {}
        for index, value in enumerate(nums):
            if value in d and (target - value) in d:
                return [d[value], index]
            
            d[value] = index
            
            if (target - value) in d and d[value] != d[target - value]:
                if (d[value] > d[target - value]):
                    return [d[target - value], d[value]]
                else:
                    return [d[value], d[target - value]]
        return [0, 0]
    
if __name__ == '__main__':
    solution = Solution()
    print(solution.twoSum(nums=[2,7,11,15], target=9) == [0,1])
    print(solution.twoSum(nums=[3,2,4], target=6) == [1,2])
    print(solution.twoSum(nums=[3,3], target=6) == [0,1])