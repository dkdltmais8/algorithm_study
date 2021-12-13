from collections import deque
def solution(bridge_length, weight, truck_weights):
    answer = 0
    success = []
    ing = deque([0]*bridge_length)
    totalTruck = len(truck_weights)
    totalWeight = 0
    while len(success)<totalTruck:
        answer += 1
        now = ing.popleft()
        if now != 0:
            success.append(now)
            totalWeight-=now
        if truck_weights:
            if totalWeight + truck_weights[0] <= weight:
                ing.append(truck_weights.pop(0))
                totalWeight += ing[-1]
            else:
                ing.append(0)
    return answer
solution(2,	10,	[7,4,5,6])