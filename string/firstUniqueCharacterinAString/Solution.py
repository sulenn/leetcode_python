class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        tempStr = ""
        for index, value in enumerate(s):
            if value not in tempStr and s.count(value) == 1:
                return index
            elif value not in tempStr:
                tempStr += value
        return -1

if __name__ == '__main__':
    s = Solution()
    print s.firstUniqChar("leetcode")
    print s.firstUniqChar("loveleetcode")