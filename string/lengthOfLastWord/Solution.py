class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        wordList = s.split(" ")
        wordList = wordList[::-1]
        for i in wordList:
            if i:
                return len(i)
        return 0

if __name__ == '__main__':
    s = Solution()
    print s.lengthOfLastWord("a ")
    print s.lengthOfLastWord("a")
    print "   aaa aaa   ".lstrip(' ')