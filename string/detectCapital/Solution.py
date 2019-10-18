class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if not word:
            return False
        if word[0].islower():
            if word.islower():
                return True
        else:
            if word.isupper():
                return True
            elif word[1:].islower():
                return True
        return False

    # def detectCapitalUse(self, word):
    #     """
    #     :type word: str
    #     :rtype: bool
    #     """
    #     return word.upper()==word or word.lower()==word or word.title()==word