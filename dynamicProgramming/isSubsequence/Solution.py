class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        for _s in s:
            if _s in t:
                index = t.index(_s)
                t = t[index+1:]
            else:
                return False
        return True

if __name__ == '__main__':
    if not "":
        print "xixi"