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
