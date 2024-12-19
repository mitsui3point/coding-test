"""
(1) 문제 이해
  input: nums {4,1,9,7,5,3,16}, target 14
  output: True
  input: nums {2,1,5,7}, target 4
  output: False
  2 <= nums.length <= 10^4
  -10^9 <= nums[i] <= 10^9
  -10^9 <= target <= 10^9
(2) 접근 방법
  직관적으로 생각하기
    보통 완전탐색으로 시작
    문제 상황을 단순화 하여 생각하기
      - 예시 [2,7,11,15], target = 9
      - 2, 7 만 있는 경우
    문제 상황을 극한화 하여 생각하기
      - 예시 [2,7,11,15], target = 9
      - 2, 3, 5, 6, 7, ...., n, target = n - 1
  자료구조와 알고리즘 활용
    (1) 문제이해 에서 파악한 내용을 토대로 어떤 자료구조를 사용하는게 가장 적합한지를 결정
    대놓고 특정 자료구조와 알고리즘을 묻는 문제도 많음
    자료구조에 따라 선택할 수 있는 알고리즘을 문제에 적용
"""
class Solution:
    def twoSum(self, nums, target):
        sortNums = list(nums)
        sortNums.sort()
        print(nums)
        print(sortNums)
        
        left = 0
        right = len(nums) - 1
        result = [0, 0]
        isFinish = True
        while isFinish:
            sum = sortNums[left] + sortNums[right]
            print(sum)
            print(left, right)
            if sum > target:
                right = right - 1
                continue
                left = left + 1
            if sum < target:
                continue
            if sum == target:
                result = [left, right]
                isFinish = False
            if right == left:
                isFinish = False
            
        print('result:'+str(result))
        if result != [0, 0]:
            sortedResult = [nums.index(sortNums[left]), nums.index(sortNums[right])]
            sortedResult.sort()
            return sortedResult
        return result

sol = Solution()
print(sol.twoSum([2,7,11,15], 9))