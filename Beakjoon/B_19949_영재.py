import sys
input = sys.stdin.readline

N = 10
sol = list(map(int, input().split()))
ans_arr = [0] * N
cnt = 0

def dfs(prob, prev_ans, streak_cnt):
    global cnt

    if streak_cnt == 3:                 # 연속 3번 같은 수로 찍었을 경우
        return

    if prob == N:                       # 맞은 개수 세기
        correct = 0
        for i in range(N):
            if sol[i] == ans_arr[i]:
                correct += 1
        if correct >= 5:
            cnt += 1
        return
    
    for j in range(1, 6):               # 문제 찍기
        ans_arr[prob] = j
        if j == prev_ans:
            dfs(prob+1, j, streak_cnt+1)
        else:
            dfs(prob+1, j, 1)

dfs(0, 0, 1)

print(cnt)