class Solution(object):

    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        return (s+s)[1:-1].find(s) != -1

    # # normal method
    # def repeatedSubstringPattern(self, s):
    #     """
    #     :type s: str
    #     :rtype: bool
    #     """
    #     if len(s) == 1:
    #         return False
    #     if s[0]*len(s) == s:  # check one character repeated
    #         return True
    #     if len(s) % 2 == 0 and s[0:len(s)//2] == s[len(s)//2:]:
    #         return True
    #     for i in range(1,len(s)//2):
    #         if len(s) % (i+1) != 0:
    #             continue
    #         else:
    #             _s = s[:i+1]*(len(s)//(i+1))
    #             if _s == s:
    #                 return True
    #     return False

if __name__ == '__main__':
    print "ads"*2
    s = Solution()
    # print s.repeatedSubstringPattern("abab")
    # print s.repeatedSubstringPattern("aba")
    # print s.repeatedSubstringPattern("abcabcabcabc")
    # print s.repeatedSubstringPattern("abcabcabc")
    # print s.repeatedSubstringPattern("ababab")
    # print s.repeatedSubstringPattern("ababab")
    print ("ababab" + "ababab")[1:-1]
    print ("ababab" + "ababab")[1:-2]
    print ("abc" + "abc")[1:-1]
    print ("ababab" + "ababab")[0:-1]
    print ("ababab" + "ababab")[0]
    print ("ababab" + "ababab")[-1]
