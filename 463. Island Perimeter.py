class Solution(object):
    def islandPerimeter(self, grid):
        l=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    l=l+4
                    if j>0 and grid[i][j-1]==1:
                            l=l-2
                    if i>0 and grid[i-1][j]==1:
                            l=l-2
        return l
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        