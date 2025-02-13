import sys
input = sys.stdin.readline

R, C, W = map(int, input().split())

# 파스칼 삼각형 만들기
pascal = []

for i in range(R+W-1):
    pascal.append([1]*(i+1))

for i in range(R+W-1):
    for j in range(1, i):
        pascal[i][j] = pascal[i-1][j-1] + pascal[i-1][j]

# 합 구하기
ans = 0

for i in range(W):
    ans += sum(pascal[R-1+i][(C-1):(C+i)])

print(ans)