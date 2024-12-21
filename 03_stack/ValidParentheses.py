class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        start = ['(', '[', '{']
        end = [')', ']', '}']

        chars = list(s)
        chars_length = len(chars)
        for char in chars:
            last_index = len(stack) - 1
            if char == start[0]:
                stack.append(char)
                continue
            if char == start[1]:
                stack.append(char)
                continue
            if char == start[2]:
                stack.append(char)
                continue
            if last_index >= 0:
                if char == end[0] and stack[last_index] == start[0]:
                    stack.pop()
                    chars_length -= 2
                    continue
                if char == end[1] and stack[last_index] == start[1]:
                    stack.pop()
                    chars_length -= 2
                    continue
                if char == end[2] and stack[last_index] == start[2]:
                    stack.pop()
                    chars_length -= 2
                    continue

        return len(stack) <= 0 and chars_length == 0
    

if __name__ == '__main__':

    solution = Solution()
    print(solution.isValid(")()") == False)
    print(solution.isValid(")(") == False)
    print(solution.isValid("()") == True)
    print(solution.isValid("()[]{}") == True)
    print(solution.isValid("(]") == False)
    print(solution.isValid("([])") == True)