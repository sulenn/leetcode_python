class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        flag = False
        num = 0
        for i in s:
            if i != " " and not flag:
                flag = True
            elif i == " " and flag:
                num += 1
                flag = False
        if flag:
            num += 1
        return num

if __name__ == '__main__':
    s = Solution()
    print s.countSegments("Hello, my name is John")
    print s.countSegments("   Hello,   my name is John   ")
