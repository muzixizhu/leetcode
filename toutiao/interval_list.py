class Solution:
    def intervalIntersection(self, A, B):
        M = len(A)
        N = len(B)
        i, j = 0, 0
        res = []
        while i < M and j < N:
            print('now {},{}, {} ,{}'.format(i, A[i],j,B[j]))
            if A[i][1] < B[j][0]:
                i += 1
            elif A[i][1] == B[j][0]:
                res.append([A[i][1], A[i][1]])
                i += 1
            elif B[j][1] == A[i][0]:
                res.append([B[j][1], B[j][1]])
                j += 1
            elif B[j][1] < A[i][0]:
                j += 1
            elif B[j][0] <= A[i][0] <= B[j][1]:
                if A[i][1] < B[j][1]:
                    res.append([A[i][0], A[i][1]])
                    i += 1
                elif A[i][1] == B[j][1]:
                    res.append([A[i][0], A[i][1]])
                    i += 1
                    j += 1
                else:
                    res.append([A[i][0], B[j][1]])
                    j += 1
            elif A[i][0] <= B[j][0] <= A[i][1]:
                if B[j][1] < A[i][1]:
                    res.append([B[j][0], B[j][1]])
                    j += 1
                elif B[j][1] == A[i][1]:
                    res.append([B[j][0], B[j][1]])
                    i += 1
                    j += 1
                else:
                    res.append([B[j][0], A[i][1]])
                    i += 1
            # print('coming here:{},{},{},{}'.format(i,j, A[i],B[j]))
        return res


if __name__=="__main__":
    # A = [[0,2],[5,10],[13,23],[24,25]]
    # B = [[1,5],[8,12],[15,24],[25,26]]
    A = [[8,15]]
    B = [[2,6],[8,10],[12,20]]
    solver = Solution()
    print(solver.intervalIntersection(A,B))