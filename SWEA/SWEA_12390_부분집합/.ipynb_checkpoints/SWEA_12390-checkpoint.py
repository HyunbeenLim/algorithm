import sys
sys.stdin = open("C:/Users/SSAFY/Desktop/스터디/SSAFY_Algorithm/SWEA/SWEA_12390/sample_input.txt", "r")
# input = sys.stdin.readline

T = int(input())
A = list(range(1, 13))
bit_length = len(A)

for tc in range(1, T + 1):
    n, k = map(int, input().split())

    cnt = 0
    for i in range(1 << bit_length): # A의 모든 부분 집합 가능성
        sub_set = []
        for j in range(bit_length): # 10 // 100 // 1000 // ... 나타내기 위함
            if i & (1 << j): # 그게 i에 포함되면 sub_set에 A[j] 추가
                sub_set.append(A[j])
        if len(sub_set) == n and sum(sub_set) == k:
            cnt += 1
    
    print(f'#{tc} {cnt}')

