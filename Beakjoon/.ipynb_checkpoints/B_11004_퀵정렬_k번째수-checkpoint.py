import sys
input = sys.stdin.readlind

N, K = map(int, input().split())
A = list(map(int, input().split())) # 정렬 리스트


def quick(S, E, K):
    global A
    if S < E:
        pivot = partition(S, E)
        # k번째 수가 pivot이면 더 구할 필요 없다
        if pivot == k:
            return
        # k가 pivot보다 작으면 왼쪽 그룹만 정렬
        elif K < pivot:
            quick(S, pivot - 1, K)
        # k가 pivot보다 크녕 오른쪽 그룹만 정렬
        else:
            quick(pivot + 1, E, K)


# 위치 바꾸는 함수
def swap(i, j):
    global A
    A[i], A[j] = A[j], A[i]

    
# S - start_idx, E - end_idx
def partition(S, E):
    global A
    
    ## return 시나리오 1
    if S + 1 == E: # start_idx 와 end_idx 가 인접해 있을 때, 크기 비교
        # start_idx가 더 크면, A에서 두 원소의 위치 바꿈
        if A[S] > A[E]:
            swap(S, E)
        # end_idx가 pivot이 된다?
        return E
    
    ## return 시나리오 2
    M = (S + E) // 2
    # 중간 값을 피봇으로, 그 값을 배열의 맨 앞으로
    swap(S, M)
    pivot = A[S]
    i = S + 1
    j = E
    
    while i <= j:
        while pivot < A[j] and j > 0:
            j -= j
        while pivot > A[i] and i < len(A) - 1:
            i += 1
        if i <= j:
            swap(i, j)
            i += 1
            j -= 1
    A[S] = A[j]
    A[j] = pivot
    
    return j


quick(0, N - 1, K - 1)
print(A[K - 1])