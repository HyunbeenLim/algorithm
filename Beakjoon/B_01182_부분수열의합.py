# N개의 정수로 이루어진 수열
# 길이가 양수인 부분 수열의 합이 S인 경우의 수 구하기
import sys
input = sys.stdin.readline

N, S = map(int, input().split())
arr = list(map(int, input().split()))
cnt = 0

def dfs(k, value):
    global cnt

    if k == N:
        if value == S:
            cnt += 1
        return
    
    dfs(k + 1, value + arr[k])
    dfs(k + 1, value)

dfs(0, 0)

if S == 0:          # 하나도 더하지 않은 경우가 존재하기 때문에 해줘야함
    cnt -= 1

print(cnt)