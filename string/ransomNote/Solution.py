class Solution(object):

    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        magazine = list(magazine)
        for i in ransomNote:
            if i in magazine:
                magazine.remove(i)
            else:
                return False
        return True

    # method with dic
    # def canConstruct(self, ransomNote, magazine):
    #     """
    #     :type ransomNote: str
    #     :type magazine: str
    #     :rtype: bool
    #     """
    #     chaDic = {}
    #     for i in magazine:
    #         if i in chaDic.keys():
    #             chaDic[i] += 1
    #         else:
    #             chaDic[i] = 1
    #     for j in ransomNote:
    #         if j not in chaDic.keys():
    #             return False
    #         else:
    #             if chaDic[j] < 1:
    #                 return False
    #             else:
    #                 chaDic[j] -= 1
    #     return True

if __name__ == '__main__':
    s = Solution()
    print s.canConstruct("a", "b")
    print s.canConstruct("aa", "ab")
    print s.canConstruct("aa", "aab")