import sys
input = sys.stdin.readline

N = int(input()) - 1
dist = [0] + list(map(int, input().split()))
price = list(map(int, input().split()))

idx = 0
spent = 0

# 일단 주유
current_price = price[idx]
spent = current_price * dist[idx + 1]

while idx < N - 1:
    idx += 1

    if price[idx] <= current_price:
        current_price = price[idx]
    
    spent += current_price * dist[idx + 1]

