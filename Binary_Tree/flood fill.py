# Flood Fill
# An image is represented by a 2-D array of integers, each integer representing the pixel value of the image (from 0 to 65535).
#
# Given a coordinate (sr, sc) representing the starting pixel (row and column) of the flood fill, and a pixel value newColor, "flood fill" the image.
#
# To perform a "flood fill", consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color as the starting pixel), and so on. Replace the color of all of the aforementioned pixels with the newColor.
#
# At the end, return the modified image.
#
# Example 1:
# Input:
# image = [[1,1,1],[1,1,0],[1,0,1]]
# sr = 1, sc = 1, newColor = 2
# Output: [[2,2,2],[2,2,0],[2,0,1]]
# Explanation:
# From the center of the image (with position (sr, sc) = (1, 1)), all pixels connected
# by a path of the same color as the starting pixel are colored with the new color.
# Note the bottom corner is not colored 2, because it is not 4-directionally connected
# to the starting pixel.
# Note:
#
# The length of image and image[0] will be in the range [1, 50].
# The given starting pixel will satisfy 0 <= sr < image.length and 0 <= sc < image[0].length.
# The value of each color in image[i][j] and newColor will be an integer in [0, 65535].
#    Show Hint #1

class Solution():
    def floodfill(self, image, sr,sc, newColor):
        Sr, SC = len(image), len(image[0])
        color = image[sr][sc]
        if color == newColor: return image
        def dfs(r,c):
            if image[r][c] == color:
                image[r][c] = newColor
                if r - 1 >= 0:dfs(r-1, c)
                if c - 1 >= 0: dfs(r, c-1)
                if r + 1 < Sr: dfs(r + 1, c)
                if c + 1 < Sc: dfs(r, c+1)
        dfs(sr, sc)
        return image

class Solution_1():
    def bfs_floodfill(self, image, sr, sc, newColor):
        dirs = [[1,0],[-1,0],[0,-1],[0,1]]
        color = image[sr][sc]
        Sr, Sc = len(image), len(image[0])
        if color == newColor: return image
        que = collections.deque()
        que.append([sr, sc])
        while que:
            r, c = que.popleft()
            if image[r][c] == color:
                image[r][c] = newColor
                for dir in dirs:
                    next_r, next_c = r + dir[0], c + dir[1]
                    if 0<=next_r<Sr and 0<=next_c<Sc:
                        que.append([next_r, next_c])
        return image