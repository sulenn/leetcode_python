class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return -1
        minute = 0 # begin bfs from original location
        curQueue = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    curQueue.append([i, j])
        while curQueue:
            nextQueue = []
            for location in curQueue:
                x = location[0]
                y = location[1]
                if x < len(grid) - 1 and grid[x+1][y] == 1:
                    grid[x + 1][y] = 2
                    nextQueue.append([x+1, y])
                if x > 0 and grid[x-1][y] == 1:
                    grid[x-1][y] = 2
                    nextQueue.append([x-1, y])
                if y < len(grid[0]) - 1 and grid[x][y+1] == 1:
                    grid[x][y+1] = 2
                    nextQueue.append([x, y+1])
                if y > 0 and grid[x][y-1] == 1:
                    grid[x][y-1] = 2
                    nextQueue.append([x, y-1])
            if not nextQueue:
                break
            curQueue = nextQueue
            minute += 1
        for row in grid:
            if 1 in row:
                return -1
        return minute

if __name__ == '__main__':
    s = Solution()
    print s.orangesRotting([[2,1,1],[1,1,0],[0,1,1]])
    print s.orangesRotting([[2,1,1],[0,1,1],[1,0,1]])