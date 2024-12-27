class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        results = []
        reverse = list(temperatures)
        reverse.reverse()
        for _ in range(len(temperatures)):
            target = reverse.pop()
            result = 0
            index = len(reverse) - 1
            while (True):
                if index == -1: break
                if index <= 0 and reverse[index] < target:
                    result = 0
                    break
                result += 1
                if reverse[index] > target: break
                index -= 1
            results.append(result)
        return results


if __name__ =='__main__':
    solution = Solution()
    # 73,74,75,71,69,72,76,73
    # 73 
    #    74,75,71,69,72,76,73
    # 
    print(solution.dailyTemperatures([73,74,75,71,69,72,76,73]) == [1,1,4,2,1,1,0,0])
    print(solution.dailyTemperatures([30,40,50,60]) == [1,1,1,0])
    print(solution.dailyTemperatures([30,60,90]) == [1,1,0])


