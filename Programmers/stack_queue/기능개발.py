from collections import deque

def solution(progress, speed):
    ans = []

    p = deque(progress)
    s = deque(speed)

    while p: 
        if p[0] >= 100:
            cnt = 0
            while p and p[0] >= 100:
                p.popleft()
                s.popleft()
                cnt += 1
            ans.append(cnt)
        
        for i in range(len(p)):
            p[i] += s[i]

    return ans

print(solution([93, 30, 55], [1, 30, 5]))
print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))