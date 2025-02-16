import sys
input = sys.stdin.readline

def dfs(idx):
    if len(lottery) == 6:
        print(*lottery)
        return
    
    for i in range(idx, K):
        lottery.append(numbers[i])
        dfs(i+1)
        lottery.pop()

while True:
    numbers = list(map(int, input().split()))

    K = numbers.pop(0)
    
    if K == 0:
        break

    lottery = []

    dfs(0)

    print()