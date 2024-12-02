import sys
input = sys.stdin.readline

N, M = map(int, input().split())

A_matrix = [[0] * (N + 1)]

for i in range(N):
    A_row = [0] + [int(x) for x in input().split()]
    A_matrix.append(A_row)

D_matrix = [[0] * (N + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    for j in range(1, N + 1):
        D_matrix[i][j] = D_matrix[i][j - 1] + D_matrix[i - 1][j] - D_matrix[i - 1][j - 1] + A_matrix[i][j]
        
for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    result = D_matrix[x2][y2] - D_matrix[x1 - 1][y2] - D_matrix[x2][y1 - 1] + D_matrix[x1 - 1][y1 - 1]
    print(result)