def solution(jobs):
    answer = []
    select = []
    time = 10001
    for i in range(len(jobs)):
        if time > jobs[i][0]:
            time = jobs[i][0]
        if jobs[i][0] == time:
            select = jobs[i]
            answer.append(select[2])
            now = select[0]+select[1]
            important = select[3]
            jobs[i] = [0]
    for i in range(len(jobs)):
        if jobs[i][0] < time:
            select.append(jobs[i])
    print(select)
    print(jobs)
    print(answer)
    print(now)
    print(important)
    return answer

solution([[1, 5, 2, 3], [2, 2, 3, 2], [3, 1, 3, 3], [5, 2, 1, 5], [7, 1, 1, 1], [9, 1, 1, 1], [10, 2, 2, 9]])