import sys
# input = sys.stdin.readline
sys.stdin = open('input.txt', 'r')

N, M = map(int, input().split())
board = [list(input().strip()) for _ in range(N)]
min_cnt = 64


def find(sr, sc):
    global min_cnt

    er, ec = sr + 8, sc + 8
    
    if er > N or ec > M:
        return False
    else:
        # 시작
        for r in range(sr, er):
            for c in range(sc, ec):
                pass
        return True

for r in range(N):
    for c in range(M):
        if find(r, c):
            print(r, c)