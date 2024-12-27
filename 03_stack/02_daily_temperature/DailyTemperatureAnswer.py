class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        answer = [0] * len(temperatures)
        print(answer)
        stack = []
        for cur_day, cur_temp in enumerate(temperatures):
            print('-----------')
            print(cur_day, cur_temp)
            print('stack',stack)
            print('answer',answer)
            while stack and stack[-1][1] < cur_temp:
                print('===')
                prev_day, _ = stack.pop()
                print(prev_day, _)
                answer[prev_day] = cur_day - prev_day
            stack.append((cur_day, cur_temp))
        return answer
    
if __name__ =='__main__':
    solution = Solution()
    
    # print(solution.dailyTemperatures([73,74,75,71,69,72,76,73]))
    print(solution.dailyTemperatures([73,74,75,71,69,72,76,73]) == [1,1,4,2,1,1,0,0])
    # print(solution.dailyTemperatures([30,40,50,60]))
    # print(solution.dailyTemperatures([30,40,50,60]) == [1,1,1,0])
    # print(solution.dailyTemperatures([30,60,90]))
    # print(solution.dailyTemperatures([30,60,90]) == [1,1,0])


