class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return True
        s = s.lower()
        newStr = ""
        for i in s:
            if 97<= ord(i) <=122 or 48 <= ord(i) <=57:
                newStr += i
        return newStr==newStr[::-1]

if __name__ == '__main__':
    s = Solution()
    print ord('a')==97
    print s.isPalindrome("A man, a plan, a canal: Panama")
    print s.isPalindrome("race a car")