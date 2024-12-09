def solution(bridge_length, weight, truck_weights):
    answer = 1
    
    bridge_q = [0] * bridge_length
    
    cur_weight = truck_weights.pop(0)
    bridge_q[bridge_length - 1] = cur_weight
    
    while truck_weights:
        answer += 1
        
        for i in range(bridge_length):
            if bridge_q[i]:
                if i == 0:                                                      # 다리 지나감
                    cur_weight -= bridge_q[i]                                   
                    bridge_q[i] = 0
                else:
                    bridge_q[i-1], bridge_q[i] = bridge_q[i], bridge_q[i-1]     # 전진
        
        if cur_weight + truck_weights[0] <= weight:                             # 다음 트럭 올리기
            new_truck = truck_weights.pop(0)
            bridge_q[bridge_length - 1] = new_truck
            cur_weight += new_truck
                    
    answer += bridge_length     # 트럭 리스트가 비는 동시에 while을 종료하기 때문에 필요함
    
    return answer

############### 시간 초과 ###############


# gpt 수정 코드
from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge_q = deque([0] * bridge_length)  # 다리를 나타내는 큐
    cur_weight = 0  # 현재 다리 위의 트럭 무게 합
    
    truck_weights = deque(truck_weights)  # 트럭 대기열을 deque로 변환

    while truck_weights or cur_weight > 0:
        answer += 1

        # 1. 다리에서 트럭이 나감
        exited_truck = bridge_q.popleft()
        cur_weight -= exited_truck

        # 2. 새 트럭이 다리에 진입할 수 있는지 확인
        if truck_weights and cur_weight + truck_weights[0] <= weight:
            new_truck = truck_weights.popleft()
            bridge_q.append(new_truck)
            cur_weight += new_truck
        else:
            bridge_q.append(0)  # 트럭이 못 들어오면 빈 공간 추가

    return answer

print(solution(2, 10, [7,4,6,5]))
print(solution(100, 100, [10]))
print(solution(100, 100, [10,10,10,10,10,10,10,10,10,10]))


### 수정 아이디어
'''
bridge_q를 다리 길이 만큼 0을 넣음
트럭이 나올 차례가 아닐 땐 트럭을 pop 하는 게 아닌, 0을 pop 하고 다시 0을 append 하는 로직
'''