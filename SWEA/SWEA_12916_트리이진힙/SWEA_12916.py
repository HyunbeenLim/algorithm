import sys
sys.stdin = open('C:/Users/SSAFY/Desktop/git/SSAFY_Algorithm/SWEA/SWEA_12916_트리이진힙/sample_input.txt', 'r')

# 최소힙
def enq(n):
    global last
    last += 1   # 마지막 노드 추가(완전이진트리 유지)
    heap[last] = n # 마지막 노드에 데이터 삽입
    c = last    # 부모>자식 비교를 위해
    p = c//2    # 부모번호 계산
    while p >= 1 and heap[p] > heap[c]:   # 부모가 있는데, 더 크면
        heap[p], heap[c] = heap[c], heap[p]  # 교환
        c = p
        p = c//2

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    numbers = list(map(int, input().split()))
    
    heap = [0]*(N+1)
    last = 0
    
    for num in numbers:
        enq(num)
    
    ans = 0
    while True:
        last = last//2
        ans += heap[last]
        if last == 1:
            break
    
    print(f'#{tc} {ans}')

    