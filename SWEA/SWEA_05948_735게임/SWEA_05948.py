import sys
sys.stdin = open('s_input.txt', 'r')

T = int(input())

ans_list = [0]

# 조합 재귀
def comb(k, s):   # s: 반복의 시작
    global sum_list
    if k == 3:
        sum_value = sum(pick)
        if sum_value not in sum_list:
            sum_list.append(sum(pick))
    else:
        remain = 3 - (k + 1)
        for i in range(s, N - remain):
            pick[k] = arr[i]
            comb(k + 1, i + 1)

for _ in range(T):
    arr = list(map(int, input().split()))
    N = len(arr)
    sum_list = []
    # 3개 뽑기
    pick = [0] * 3

    comb(0, 0)
    
    sum_list.sort()
    sum_list = sum_list[::-1]
    ans_list.append(sum_list[4])

for tc in range(1, T + 1):
    print(f'#{tc} {ans_list[tc]}')

