import sys
sys.stdin = open('sample_input.txt', 'r')

# 시작 위치 기준 m 개의 벌통만 탐색
def dfs(L, x, y, now, val):
    global temp_profit
    if now > c:
        return # 가지치기
    if L == m:
        temp_profit = max(temp_profit, val)                     # m 개의 벌통을 다 확인했다면 끝
    else:
        dfs(L + 1, x, y + 1, now + g[x][y], val + g[x][y] ** 2)
        dfs(L + 1, x, y + 1, now, val)


T = int(input())

for tc in range(1,T+1):
    n,m,c = map(int, input().split()) 
    g = [list(map(int, input().split())) for _ in range(n)]

    profit = 0
    
    # 먼저 일꾼 A를 확정짓고 시작
    profit_A = 0
    profit_B = 0
    for x1 in range(n):
        for y1 in range(n - m + 1):
            temp_profit = 0
            dfs(0, x1, y1, 0, 0)
            profit_A = temp_profit
            for x2 in range(x1, n):
                start = 0
                if x1 == x2: # 같은 행인 경우 
                    start = y1 + m # 시작위치 조정
                for y2 in range(start, n - m + 1):
                    temp_profit = 0
                    dfs(0, x2, y2, 0, 0)
                    profit_B = temp_profit
                    profit = max(profit, profit_A + profit_B)

    print(f"#{tc} {profit}")