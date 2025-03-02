import sys
# input = sys.stdin.readline
sys.stdin = open('input.txt', 'r')

N, C = map(int, input().split())
houses = []
for _ in range(N):
    houses.append(int(input()))

houses.sort()

# 현재 공유기 설치 수
cnt = 0
start, end = 0, N-1
# 한 사이클에 공유기는 2개씩 설치하기 때문에 while 종료 이후 공유기 설치 수가 C보다 1 커도 답엔 영향 X
while cnt < C:
    middle = (start + end) // 2

    if middle in (start, end):
        break

    # 최대, 최소에 공유기 설치
    cnt += 2

    if abs(houses[start]-houses[middle]) < abs(houses[end]-houses[middle]):
        current_min_dist = abs(houses[start]-houses[middle])
        start = middle
        end -= 1
    else:
        current_min_dist = abs(houses[end]-houses[middle])
        end = middle
        start += 1

print(current_min_dist)