def solution(n, times):
    times.sort()

    # 최소, 최대 시간 정의의
    start = times[0]
    end = max(times) * n

    while start < end:
        middle = (start + end) // 2

        # 중간 값에서 모든든 입국 심사대가 처리할 수 있는 사람 수
        done = sum(middle // time for time in times)
        
        if done >= n:
            end = middle
        elif done < n:
            start = middle + 1
    
    min_time = start
    # start부터 1씩 줄여가며 최소 시간 찾기
    for t in range(start - 1, 0 , -1):
        done = sum(t // time for time in times)
        if done == n:
            min_time = t
        else:
            return min_time

print(solution(6, [7, 10]))