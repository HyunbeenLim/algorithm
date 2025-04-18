def solution(routes):
    # route[i][1] 기준 정렬

    routes = sorted(routes, key=lambda x:x[1])

    cam_cnt = 0
    # 초기값 설정
    current_cam = -30001

    for car in routes:
        # 현재 카메라의 위치가 차의 진입 위치보다 크거나 같다면 설치 X
        if car[0] <= current_cam:
            continue
        # 카메라의 위치가 차의 진입 위치보다 작다면 차의 진출 시점에 카메라 설치, 카메라 위치 업데이트
        else:
            cam_cnt += 1
            current_cam = car[1]

    return cam_cnt

print(solution([[-20,-15], [-14,-5], [-18,-13], [-5,-3]])) # 2