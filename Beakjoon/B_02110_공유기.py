import sys
# input = sys.stdin.readline
sys.stdin = open('input.txt', 'r')

N, C = map(int, input().split())
houses = []
for _ in range(N):
    houses.append(int(input()))
houses.sort()

s = 1
e = houses[-1] - houses[0]

# s가 e 이하일 때까지만(같을 때도 동작)
while s <= e:
    m = (s + e) // 2
    cnt = 1
    installed = houses[0]

    # 앞에서부터 순회
    ## 이전 설치 장소에서 m 이상 떨어진 집에 다시 설치하면서 count
    for i in range(1, N):
        if houses[i] >= installed + m:
            cnt += 1
            installed = houses[i]

    # 목표 설치 수보다 작다면, 거리를 줄여 더 설치해야 함
    if cnt < C:
        e = m - 1
    # 목표 설치 수보다 크거나 같다면 거리를 늘림
    ## 같을 때도 늘리는 이유는, 최적 값을 찾기 위함 => 그래서 이진 탐색을 하는 것
    else:
        s = m + 1
        ans = m

print(ans)


