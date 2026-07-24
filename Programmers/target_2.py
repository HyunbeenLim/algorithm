## 시간 더 짧게
## 이전 코드에 있던 rest_sum을 미리 만들어둔 리버스 누적합 리스트에서 가져오면서 확인하기
def solution(numbers, target):

    suffix_sum = [0] * (len(numbers) + 1)

    for i in range(len(numbers)-1, -1, -1):
        suffix_sum[i] = numbers[i] + suffix_sum[i+1]

    def dfs(level, current_value):
        rest_sum = suffix_sum[level]
        # 가지치기
        if current_value - rest_sum > target:
            return 0
        elif current_value + rest_sum < target:
            return 0

        # 종료 조건
        if level == len(numbers):
            return 1 if current_value == target else 0
        
        return dfs(level + 1, current_value + numbers[level]) + dfs(level + 1, current_value - numbers[level])

    return dfs(0, 0)

print(solution([1, 1, 1, 1, 1], 3))
print(solution([4, 1, 2, 1], 4))