class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for p in s:
            if p == '(':
                stack.append(')')
                continue
            if p == '[':
                stack.append(']')
                continue
            if p == '{':
                stack.append('}')
                continue
            if not stack or stack.pop() != p:
                return False
            
        return not stack
    

if __name__ == '__main__':

    solution = Solution()
    print(solution.isValid(")()") == False)
    print(solution.isValid(")(") == False)
    print(solution.isValid("()") == True)
    print(solution.isValid("()[]{}") == True)
    print(solution.isValid("(]") == False)
    print(solution.isValid("([])") == True)