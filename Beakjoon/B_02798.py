import sys
input = sys.stdin.readline

#### 부끄러운 나의 코드

N, M = map(int, input().split())

cards = list(map(int, input().split()))

def cards_sum():
    sum_list = []
    # 3장 찾기(비효율적 ㅜㅜ)
    for i in range(N-2):
        for j in range(i+1, N-1):
            for k in range(j+1, N):
                sum_value = cards[i] + cards[j] + cards[k]
                if sum_value <= M:
                    sum_list.append(sum_value)
    
    return max(sum_list)

print(cards_sum())



#### 현준이형 재귀

max_sum = float('-inf')
def backtrack(idx, cur_cnt, cur_sum):
    global limit, max_sum
    
    if cur_cnt > 3:
        return
    
    if cur_sum > limit:
        return
    
    if idx == N:
        if cur_cnt == 3 and cur_sum <= limit:
            max_sum = max(max_sum, cur_sum)
    else:
        visited[idx] = 1
        backtrack(idx + 1, cur_cnt + 1, cur_sum + card_lst[idx])
        
        visited[idx] = 0
        backtrack(idx + 1, cur_cnt, cur_sum)

N, limit = map(int, input().split())
card_lst = list(map(int, input().split()))

visited = [0] * N

backtrack(0, 0, 0)
print(max_sum)
