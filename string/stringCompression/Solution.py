class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        i = 1
        tempCha = chars[0]
        index = 0
        for j in chars[1:]:
            if j == tempCha:
                i += 1
            elif i > 1:
                chars[index] = tempCha
                index += 1
                i_str = str(i)
                for z in i_str:
                    chars[index] = z
                    index += 1
                tempCha = j
                i = 1
            else:
                chars[index] = tempCha
                index += 1
                tempCha = j
                i = 1
        if i == 1:
            chars[index] = tempCha
            index += 1
        else:
            chars[index] = tempCha
            index += 1
            i_str = str(i)
            for z in i_str:
                chars[index] = z
                index += 1
        return index

if __name__ == '__main__':
    print "a"[1:]
    s = Solution()
    print s.compress(["a","b","b","b","b","b","b","b","b","b","b","b","b"])
    print s.compress(["a"])
    print s.compress(["a","a","b","b","c","c","c"])
