import sys
# input = sys.stdin.readline
sys.stdin = open('input.txt', 'r')

# 우 하 좌 상
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]



N = 5
seats = [list(input().strip()) for _ in range(N)]
visited = [[0] * N for _ in range(N)]
path = []
cnt = 0



for path_i in path:
    print(path_i)
print(cnt)