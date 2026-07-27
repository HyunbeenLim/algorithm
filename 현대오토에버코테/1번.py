def solution(dataSize, processingTime):
    N = len(dataSize)

    # [누적 사용량, 끝나는 시간]
    servers = [[dataSize[0], processingTime[0]-1]]
    # 최대 누적 사용량
    max_cum = dataSize[0]

    for t in range(1, N):
        available = -1
        min_size = 10001

        # 사용 가능한 서버인지 확인
        for i in range(len(servers)):
            server = servers[i]
            if (server[1] < t) and (server[0] < min_size):
                available = i
                min_size = min(min_size, server[0])

        # 사용 가능한 서버가 없다면 새로운 서버 열기
        if available == -1:
            servers.append([dataSize[t], t+processingTime[t]-1])
            max_cum = max(max_cum, dataSize[t])

        else:
            servers[available][0] += dataSize[t]
            servers[available][1] = t+processingTime[t]-1
            max_cum = max(max_cum, servers[available][0])

    return max_cum

print(solution([2,7,4], [5,5,5]))

#### 정답 코드는 아래 
import heapq


def solution(dataSize, processingTime):
    # (누적 처리량, server_id)
    available = []

    # (종료 시각, server_id, 누적 처리량)
    busy = []

    next_server_id = 0
    max_cum = 0

    for t, (size, ptime) in enumerate(zip(dataSize, processingTime)):

        # t초부터 다시 사용할 수 있는 서버 반환
        while busy and busy[0][0] < t:
            _, server_id, cumulative = heapq.heappop(busy)
            heapq.heappush(available, (cumulative, server_id))

        if available:
            # 누적 처리량이 가장 작은 서버 선택
            cumulative, server_id = heapq.heappop(available)
            cumulative += size

        else:
            # 새 서버 생성
            server_id = next_server_id
            next_server_id += 1
            cumulative = size

        finish_time = t + ptime - 1

        heapq.heappush(
            busy,
            (finish_time, server_id, cumulative)
        )

        max_cum = max(max_cum, cumulative)

    return max_cum