class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        elements = {}
        max = None
        for _, value in enumerate(nums):
            elements[value] = 1
        
        for element in elements:
            compare = element
            while True:
                if compare + 1 in elements:
                    compare += 1
                    elements[element] += 1
                else:
                    break
            if (max == None) or (elements[element] > max):
                max = elements[element]
        
        return max

if __name__ == '__main__':
    solution = Solution()
    print(solution.longestConsecutive([100,4,200,1,3,2]) == 4)
    print(solution.longestConsecutive([0,3,7,2,5,8,4,6,0,1]) == 9)
    print(solution.longestConsecutive([1,2,0,1]) == 3)
    print(solution.longestConsecutive([1,2,0,1,4,6,7,5]) == 4)
    print(solution.longestConsecutive([0]) == 1)
    print(solution.longestConsecutive([0,0]) == 1)