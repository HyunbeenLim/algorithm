import sys
sys.stdin = open('C:/Users/SSAFY/Desktop/git/SSAFY_Algorithm/SWEA/SWEA_12914_subtree/sample_input.txt', 'r')

from collections import deque

# 숫자세기
def bfs(sub_root):
    q = deque()
    q.append(sub_root)
    
    cnt = 1
    while q:
        p = q.popleft()
        
        # 왼쪽 자식 세기
        if left[p] != 0:
            q.append(left[p])
            cnt += 1
        # 오른쪽 자식 세기
        if right[p] != 0:
            q.append(right[p])
            cnt += 1
    return cnt

T = int(input())

for tc in range(1, T + 1):
    E, N = map(int, input().split())
    
    left = [0] * (E + 2)
    right = [0] * (E + 2)
    
    arr = list(map(int, input().split()))
    
    # 자식-부모 리스트
    for i in range(E):
        p, c = arr[i*2], arr[i*2+1]
        
        if left[p] == 0:
            left[p] = c
        else:
            right[p] = c
    
    ans = bfs(N)
    
    print(f'#{tc} {ans}')