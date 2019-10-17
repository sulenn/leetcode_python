class Solution(object):
    # best method
    def longestCommonPrefix(self, strs):
        if not strs:
            return ''
        max_word = max(strs)
        min_word = min(strs)
        for index, item in enumerate(min_word):
            if item != max_word[index]:
                return max_word[:index]
        return min_word

    # def longestCommonPrefix(self, strs):
    #     """
    #     :type strs: List[str]
    #     :rtype: str
    #     """
    #     s = ""
    #     for i in zip(*strs):
    #         if len(set(i)) == 1:
    #             s += i[0]
    #         else:
    #             return s
    #     return s

    # # normal method
    # def longestCommonPrefix(self, strs):
    #     """
    #     :type strs: List[str]
    #     :rtype: str
    #     """
    #     if not strs:
    #         return ""
    #     # minimum = strs[0]
    #     # for i in strs:
    #     #     if len(minimum) > len(i):
    #     #         minimum = i
    #     minimum = min(strs,key=len)
    #     j = 0
    #     while j < len(minimum):
    #         flag = False
    #         for i in strs:
    #             if minimum[j] != i[j]:
    #                 flag = True
    #                 break
    #         if flag:
    #             break
    #         j += 1
    #     return minimum[0:j]

if __name__ == '__main__':
    s = Solution()
    # print s.longestCommonPrefix(["flower","flow","flight"])
    # print s.longestCommonPrefix(["dog","racecar","car"])
    # print s.longestCommonPrefix(["a","a","b"])
    print min(["flowe","flow","flight"])
    print min(["flower","flow"])
