
def solution(nums):
    n = len(nums)
    unique = len(set(nums))
    
    return min(unique, n//2)


print(solution([3,1,2,3]))
print(solution([3,3,3,2,2,4]))
print(solution([3,3,3,2,2,2]))