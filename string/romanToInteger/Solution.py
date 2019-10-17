class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        romanDic = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        curNum = 0
        sum = 0
        i = len(s) - 1
        while i >= 0:
            if romanDic[s[i]] < curNum:
                sum -= romanDic[s[i]]
            else:
                sum += romanDic[s[i]]
            curNum = romanDic[s[i]]
            i -= 1
        return sum
if __name__ == '__main__':
    s = Solution()
    print s.romanToInt("III")
    print s.romanToInt("IV")
    print s.romanToInt("IX")
    print s.romanToInt("LVIII")