from collections import deque
def solution(bridge_length, weight, truck_weights):
    answer = 0
    #도착한 트럭
    success = []
    #다리를 지나는 상태
    ing = deque([0]*bridge_length)
    #트럭의 개수
    totalTruck = len(truck_weights)
    #다리 위의 트럭의 무게 총합
    totalWeight = 0
    #모든 트럭이 성공하지 않으면 계속 반복
    while len(success)<totalTruck:
        #시간 증가
        answer += 1
        #이번 차례에 끝나는 게 트럭인지 빈 공간인지 체크 하기 위한 변수
        now = ing.popleft()
        # 트럭이 도착했을 때
        if now != 0:
            #성공한 리스트에 추가
            success.append(now)
            #현재 다리에서 트럭의 무게 제거
            totalWeight-=now
        # 아직 출발안한 트럭이 있는 경우
        if truck_weights:
            #다리위에 새로운 트럭이 출발 할 수 있을 때
            if totalWeight + truck_weights[0] <= weight:
                #트럭을 추가
                ing.append(truck_weights.pop(0))
                #다리위의 무게를 추가
                totalWeight += ing[-1]
            #다리의 무게과 초과되었을 때
            else:
                #트럭대신 공기로 채움
                ing.append(0)
        # print(ing)
    return answer
solution(2,	10,	[7,4,5,6])