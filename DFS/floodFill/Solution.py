class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        if sr < 0 or sr >= len(image) or sc < 0 or sc >= len(image[0]):
            return image
        else:
            if image[sr][sc] == newColor:   # judge newColor value == image[sr][sc]
                return image
            return self.floodFillRecursive(image, sr,sc,newColor,image[sr][sc])

    def floodFillRecursive(self, image, sr, sc, newCol0r, originalColor):
        if sr < 0 or sr > len(image) - 1 or sc < 0 or sc > len(image[0]) - 1:
            return image
        image[sr][sc] = newCol0r
        if sr > 0 and image[sr - 1][sc] == originalColor:
            image = self.floodFillRecursive(image, sr - 1,sc, newCol0r,originalColor)
        if sc > 0 and image[sr][sc - 1] == originalColor:
            image = self.floodFillRecursive(image, sr, sc - 1, newCol0r, originalColor)
        if sc < len(image[0]) - 1 and image[sr][sc + 1] == originalColor:
            image = self.floodFillRecursive(image, sr, sc + 1, newCol0r, originalColor)
        if sr < len(image) - 1 and image[sr + 1][sc] == originalColor:
            image = self.floodFillRecursive(image, sr + 1, sc, newCol0r, originalColor)
        return image

if __name__ == '__main__':
    s = Solution()
    # print s.floodFill([[1,1,1],[1,1,0],[1,0,1]], 1, 1, 2)
    # print s.floodFill([[0,1,0],[0,1,0]], 1, 1, 1)
    # print s.floodFill([[0,0,0],[0,1,0]], 0, 0, 2)
    print s.floodFill([[0,0,0],[0,1,0]], 1, 1, 2)