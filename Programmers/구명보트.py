def solution(weights, limit):
    left = 0
    right = len(weights) - 1
    weights.sort()
    
    cnt = 0
    while left <= right:
        
        if weights[left] + weights[right] <= limit:
            left += 1
            right -= 1
        else:
            right -= 1
        
        cnt += 1

    return cnt

print(solution([70, 50, 80, 50], 100))
print(solution([70, 80, 50], 100))