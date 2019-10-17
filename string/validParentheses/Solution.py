class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return True
        parentheseDic = {")":"(", "]":"[", "}":"{"}
        stack = []
        for i in s:
            if i in parentheseDic.values():
                stack.append(i)
            else:
                if stack and stack[-1] == parentheseDic[i]:
                    stack.pop()
                else:
                    return False
        return not stack

if __name__ == '__main__':
    s = Solution()
    print s.isValid("()")
    print s.isValid("(]")
    print s.isValid("([)]")