def solution(N):
    used = 0

    while N > 0:
        if N % 2 == 1:
            N -= 1
            used += 1
        
        N //= 2
    
    return used


print(solution(5))
print(solution(6))
print(solution(5000))