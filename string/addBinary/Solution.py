class Solution(object):

    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        return str(bin(int(a,2)+int(b,2)))[2:]

    # # normal method
    # def addBinary(self, a, b):
    #     """
    #     :type a: str
    #     :type b: str
    #     :rtype: str
    #     """
    #     if len(a)>len(b):
    #         a, b = b, a
    #     for i in range(len(b)-len(a)):
    #         a = "0" + a
    #     a = a[::-1]
    #     b = b[::-1]
    #     temp = 0
    #     sum = ""
    #     for index, value in enumerate(a):
    #         curValue = (int(value) + temp + int(b[index])) % 2
    #         temp = (int(value) + temp + int(b[index])) // 2
    #         sum += str(curValue)
    #     if temp == 1:
    #         sum += str(temp)
    #     return sum[::-1]

if __name__ == '__main__':
    s = Solution()
    print s.addBinary("11", "1")
    print s.addBinary("1010", "1011")