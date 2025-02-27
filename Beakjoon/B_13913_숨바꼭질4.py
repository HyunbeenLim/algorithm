import sys
# input = sys.stdin.readline
sys.stdin = open('input.txt', 'r')
from collections import deque

n, k = map(int, input().split())
visited = [[0, 0] for _ in range(100001)]   # visited[i][0] -> i를 방문할 때까지 걸린 최소 시간 저장 + 방문 여부 확인
                                            # visited[i][1] -> i를 최소 시간으로 방문했을 때의 이전 좌표

# 최소 시간 구하기
def bfs():
    global visited

    q = deque()
    visited[n][0] = 1
    q.append(n)

    while q:
        x = q.popleft()
        if x == k:
            print(visited[x][0] - 1)
            return

        for nx in (x-1, x+1, 2*x):
            # 처음에 < 100000으로 했다가 계속 틀렸음!
            if (0 <= nx <= 100000) and not visited[nx][0]:
                visited[nx][0] = visited[x][0] + 1
                visited[nx][1] = x
                q.append(nx)

# 경로 찾기
def find_path():
    current_pos = k
    path = [current_pos]

    # 경로 역추적
    ## 걸린 시간만큼 반복하면, n == k일 때도 정상적으로 작동
    for _ in range(visited[k][0]-1):
        prev_pos = visited[current_pos][1]
        path.append(prev_pos)
        current_pos = prev_pos

    # 이거 있는지 몰랐음
    path.reverse()
    
    print(*path)
    return

bfs()
find_path()