import sys
input = sys.stdin.readline

from collections import deque
from itertools import combinations

# 최소 인구 업데이트 함수
def cal_diff(subset_1, subset_2):
    global min_diff
    
    # 선거구 1과 2의 인구 합을 계산
    pop_1 = sum(pops[idx] for idx in subset_1)
    pop_2 = sum(pops[idx] for idx in subset_2)
    
    # 인구 차이
    diff = abs(pop_1 - pop_2)
    
    # 최소 인구 차이 갱신
    min_diff = min(min_diff, diff)
        
    return min_diff

# 인접 확인 함수
def bfs(subset):
    if not subset:
        return False
    
    q = deque()
    q.append(subset[0])
    
    # 방문리스트
    visited = [0] * (N + 1)
    visited[subset[0]] = 1
    # 개수 확인
    cnt = 1
    
    while q:
        # 부모 노드
        parent = q.popleft()
        
        # 탐색
        for child in neighbor[parent]:
            # 자식 노드가 부분 집합에 포함되어 있고, 방문한적 없다면
            if child in subset and not visited[child]:
                visited[child] = 1
                cnt += 1
                q.append(child)
                
    # cnt와 부분 집합의 길이가 같다면 해당 선거구는 모두 연결되어 있다
    return len(subset) == cnt
        

N = int(input())    # 구역 수
nodes = list(range(1, N + 1))    # 노드
pops = [0] + list(map(int, input().split()))    # 구역 별 인구

# 인접리스트
neighbor = [0]
for _ in range(N):
    number, *node = list(map(int, input().split()))    # number는 인접한 노드의 개수를 나타내는데, len() 함수를 쓰는 것보다 유의미하게 빠를까?
    neighbor.append(node)

min_diff = 100 * N  # 백준시가 가질 수 있는 최대 인구

# 부분집합을 만들어서 확인하자
for limit in range(1, N // 2 + 1):                          # subset_1의 길이를 제한해 중복을 피하자
    for subset_1 in combinations(nodes, limit):
        subset_1 = list(subset_1)
        if bfs(subset_1):                                   # subset_1이 유효하다면 subset_2
            subset_2 = [x for x in nodes if x not in subset_1]
            if bfs(subset_2):                               # subset_2도 유효하다면 차이 구하기
                cal_diff(subset_1, subset_2)

if min_diff == 100 * N:
    min_diff = -1

print(min_diff)
