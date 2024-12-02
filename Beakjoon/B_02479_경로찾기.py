import sys
input = sys.stdin.readline
# sys.stdin = open('input.txt', 'r')
from collections import deque

# 두 이진수 코드의 해밍 거리 구하는 함수
def cal_dist(a, b):
    dist = 0
    for i in range(K):
        if a[i] != b[i]:
            dist += 1
    return dist

def bfs(s, e):
    q = deque()
    q.append((s, [s]))
    visited = [0] * (N + 1)
    visited[s] = 1
    
    while q:
        node, path = q.popleft()

        if node == e:
            return path

        for child in graph[node]:
            if not visited[child]:
                visited[child] = 1
                q.append((child, path + [child]))
    
    return -1
    

N, K = map(int, input().split())

bit_list = [0]

for _ in range(N):
    bit_list.append(list(map(int, input().strip())))

# 인접 리스트(해밍 거리가 서로 1인 노드들 저장)
graph = [[] for _ in range(N + 1)]

for i in range(1, N + 1):
    for j in range(i + 1, N + 1):
        if cal_dist(bit_list[i], bit_list[j]) == 1:
            graph[i].append(j)
            graph[j].append(i)

start, end = map(int, input().split())

ans = bfs(start, end)

if ans == -1:
    print(ans)
else:
    for node in ans:
        print(node, end=' ')