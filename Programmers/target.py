def solution(numbers, target):

    def dfs(level, current_value, rest_sum):

        # 가지치기
        if current_value - rest_sum > target or current_value + rest_sum < target:
            return 0

        # 종료 조건
        if level == len(numbers):
            return 1 if current_value == target else 0
        
        return dfs(level + 1, current_value + numbers[level], rest_sum - numbers[level]) + dfs(level + 1, current_value - numbers[level], rest_sum - numbers[level])

    return dfs(0, 0, sum(numbers))

print(solution([1, 1, 1, 1, 1], 3))
print(solution([4, 1, 2, 1], 4))