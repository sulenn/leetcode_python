class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if len(num1) > len(num2):
            num1, num2 = num2, num1
        for i in range(len(num2) - len(num1)):
            num1 = "0" + num1
        temp = 0
        newNum = ""
        num1 = num1[::-1]
        num2 = num2[::-1]
        for i in range(len(num1)):
            rest = (int(num1[i]) + temp + int(num2[i])) % 10
            temp = (int(num1[i]) + temp + int(num2[i])) // 10
            newNum += str(rest)
        if temp == 1:
            newNum += str(temp)
        return newNum[::-1]

if __name__ == '__main__':
    s = Solution()
    print s.addStrings("19","1")
    print s.addStrings("99","1")
