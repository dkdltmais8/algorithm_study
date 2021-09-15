def solution(numbers):
    answer = []
    d = len(numbers)
    for i in range(d):
        for j in range(d):
            if i == j:
                continue
            else:
                answer.append(numbers[i]+numbers[j])
    answer = list(set(answer))
    return sorted(answer)