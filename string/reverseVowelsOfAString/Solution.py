class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = list(s)
        i = 0
        j = len(s) - 1
        vowelList = 'aeiouAEIOU'
        while i < j:
            if s[i] in vowelList and s[j] in vowelList:
                s[i], s[j] = s[j], s[i]
                i += 1
                j -= 1
            if s[i] not in vowelList:
                i += 1
            if s[j] not in vowelList:
                j -= 1
        return "".join(s)

if __name__ == '__main__':
    s = Solution()
    # print s.reverseVowels("hello")
    print s.reverseVowels("leetcode")