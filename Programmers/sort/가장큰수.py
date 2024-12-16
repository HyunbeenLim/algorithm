def solution(numbers):
    numbers = list(map(str, numbers))
    answer = ''
    
    while numbers:
        max_index, max_value = max(enumerate(numbers), key=lambda x: x[1][0])
        answer += max_value
        numbers.pop(max_index)
    
    return answer

print(solution([6, 10, 2]))
print(solution([3, 30, 34, 5, 9]))