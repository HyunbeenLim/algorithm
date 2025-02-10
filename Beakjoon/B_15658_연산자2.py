import sys
input = sys.stdin.readline

def divide(a, b):
    if a >= 0:
        return int(a/b)
    else:
        return -int(-a/b)
    
def dfs(idx, value):
    global min_value, max_value, operator

    if idx == N:
        max_value = max(value, max_value)
        min_value = min(value, min_value)
        return
    
    for i in range(4):
        if operator[i]:
            operator[i] -= 1
            if i == 0:
                dfs(idx+1, value+number[idx])
            elif i == 1:
                dfs(idx+1, value-number[idx])
            elif i == 2:
                dfs(idx+1, value*number[idx])
            else:
                dfs(idx+1, divide(value, number[idx]))
            operator[i] += 1

N = int(input())

number = list(map(int, input().split()))
operator = list(map(int, input().split()))

max_value = -1e9 - 1
min_value = 1e9 + 1

dfs(1, number[0])

print(max_value)
print(min_value)

