# 200
# https://leetcode.com/problems/number-of-islands/
class Solution:
    rows = 0
    cols = 0
    numIslands = 0
    grid = []

    def dfs(self, row, col):
        if row < 0 or col < 0 or row >= self.rows or col >= self.cols:
            return

        if self.grid[row][col] == '0':
            return

        elif self.grid[row][col] == '1':
            self.grid[row][col] = '0'
            self.dfs(row-1, col)
            self.dfs(row+1, col)
            self.dfs(row, col-1)
            self.dfs(row, col+1)


    def numIslands(self, grid: List[List[str]]) -> int:
        self.rows = len(grid)
        self.cols = len(grid[0])
        self.numIslands = 0
        self.grid = grid[:]

        for row in range(self.rows):
            for col in range(self.cols):
                if self.grid[row][col] == '1':
                    self.numIslands += 1
                    self.dfs(row, col)

        return self.numIslands




