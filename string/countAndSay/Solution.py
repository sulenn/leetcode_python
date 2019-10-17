class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        i = 1
        result = "1"
        while i < n:
            result = self.recursive(result)
            i += 1
        return result
    def recursive(self, s):
        result = ""
        num = 0
        curValue = 0
        for i in list(s):
            if not curValue:
                curValue = i
                num += 1
            else:
                if i == curValue:
                    num += 1
                else:
                    result += str(num)+curValue
                    num = 1
                    curValue = i
        result += str(num) + curValue
        return result

if __name__ == '__main__':
    s = Solution()
    print s.countAndSay(4)
    print list("1234")
