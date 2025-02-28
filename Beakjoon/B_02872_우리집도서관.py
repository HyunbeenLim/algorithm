import sys
# input = sys.stdin.readline
sys.stdin = open('input.txt', 'r')

N = int(input())

numbers = []
for _ in range(N):
    numbers.append(int(input()))

max_num = numbers[0]
max_idx = 0

# 가장 큰 수 찾기기
for i in range(1, N):
    if max_num < numbers[i]:
        max_num = numbers[i]
        max_idx = i

# 가장 큰 수를 기준으로 인덱스를 낮춰가면서 1 작은 수 찾기, 찾으면 오름차순 count 올려주고, 그 수를 가장 큰 수로 업데이트
ascending_count = 1
for j in range(max_idx-1, -1, -1):
    if max_num - 1 == numbers[j]:
        ascending_count += 1
        max_num = numbers[j]

print(N-ascending_count)