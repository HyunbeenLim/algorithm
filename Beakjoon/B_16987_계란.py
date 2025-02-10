import sys
input = sys.stdin.readline

def dfs(idx):
    global max_crush, eggs

    if idx == N:
        cnt = 0
        for egg in eggs:
            if egg[0] <= 0:
                cnt += 1
        max_crush = max(max_crush, cnt)
        return
    
    if eggs[idx][0] <= 0:
        dfs(idx+1)
        return
    
    for i in range(N):
        if i == idx or eggs[i][0] <= 0:
            continue
        # 계란 치기
        eggs[i][0] -= eggs[idx][1]
        eggs[idx][0] -= eggs[i][1]

        dfs(idx+1)

        # 다시 복구
        eggs[i][0] += eggs[idx][1]
        eggs[idx][0] += eggs[i][1]

    # 계란을 한번도 치지 않았을 때 
    else:
        cnt = 0
        for egg in eggs:
            if egg[0] <= 0:
                cnt += 1
        max_crush = max(max_crush, cnt)
        return


N = int(input())
eggs = []

for _ in range(N):
    eggs.append(list(map(int, input().split())))        # [내구도, 무게]

max_crush = 0

dfs(0)
print(max_crush)
    