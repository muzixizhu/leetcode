# Given a matrix of m x n elements (m rows, n columns),
# return all elements of the matrix in spiral order.

class Solution():
    def spiralOrder(self, matrix):
        rows = len(matrix)
        cols = len(matrix[0])
        top = 0
        left = 0
        down = rows - 1
        right =cols - 1
        res = []
        while top < down and left < right:

            for j in range(left, right + 1):
                res.append(matrix[top][j])
            top += 1
            for i in range(top, down + 1):
                res.append(matrix[i][right])
            right -= 1
            for j in range(right, left - 1, -1):
                res.append(matrix[down][j])
            down -= 1
            for i in range(down, top-1, -1):
                res.append(matrix[i][left])
            left += 1
        if top == down and left < right:
            for i in range(left, right + 1):
                res.append(matrix[top][i])
        elif top < down and left == right:
            for j in range(top, down + 1):
                res.append(matrix[j][left])

        return res


def run():
    matrix = [[1, 2, 3, 4],
              [5, 6, 7, 8],
              [9, 10, 11, 12]]
    matrix_1 = [[1,2,3],
                [4,5,6],
                [7,8,9],
                [10,11,12]]
    solver = Solution()
    print(solver.spiralOrder(matrix))
    print(solver.spiralOrder(matrix_1))

if __name__=="__main__":
    run()


