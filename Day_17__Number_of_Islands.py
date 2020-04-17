'''
Problem Statement -> 
        Given a 2d grid map of '1's (land) and '0's (water),
        count the number of islands. An island is surrounded
        by water and is formed by connecting adjacent lands 
        horizontally or vertically. You may assume all four 
        edges of the grid are all surrounded by water.

Example 1:
        Input:
        11110
        11010
        11000
        00000

        Output: 1
'''

# Solution - Using DFS : Time O(n*m), Space O(n,m)


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if grid is None or len(grid) == 0:
            return 0
        islandCount =0
        land_set = set()
        
        def helper(x,y):
            if (x,y) in land_set:
                return 0
            land_set.add((x,y))
            hor = y+1
            while hor < len(grid[x]) and grid[x][hor] == "1":
                helper(x,hor)
                hor += 1
                
            hor = y-1
            while  hor >= 0 and grid[x][hor] == "1":
                helper(x,hor)
                hor -=1
                
            ver = x+1
            while ver < len(grid) and grid[ver][y] == "1":
                helper(ver,y)
                ver += 1
                
            ver = x-1
            while ver >= 0 and grid[ver][y] == "1":
                helper(ver,y)
                ver -= 1
            
            return 1
                
            
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    islandCount += helper(i,j)
                                    
        return islandCount
                