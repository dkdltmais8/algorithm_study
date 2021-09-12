def solution(n, lost, reserve):
    answer = 0
    student = [1 for i in range(1,n+1)]
    # print(student)
    for i in lost:
        student[i-1] -= 1
    # print(student)
    for i in reserve:
        student[i-1] += 1
    # print(student)
    if student[0] == 0 and student[1] == 2:
        student[0] = 1
        student[1] = 1
    if student[n-1] == 0 and student[n-2] == 2:
        student[n-1] = 1
        student[n-2] = 1
    for i in range(1,n-1):
        if student[i] == 0:
            if student[i-1] == 2:
                student[i-1] = 1
                student[i] = 1
                continue
            elif student[i+1] == 2:
                student[i+1] = 1
                student[i] = 1
                continue

    # print(student)
    for i in student:
        if i >= 1:
            answer += 1
    # print(answer)
    return answer
solution(5,	[2, 4]	,[1, 3, 5])