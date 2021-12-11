from collections import deque


def solution(bridge_length, weight, truck_weights):
    answer = 0
    ing = deque([0] * bridge_length)
    while 1:
        while sum(ing) + truck_weights[0] <= weight:
            ing.popleft()
            ing.append(truck_weights.pop(0))
            answer += 1
            if not truck_weights:
                break
        if not truck_weights:
            break
        ing.popleft()
        ing.append(0)
        answer += 1

    return answer + bridge_length