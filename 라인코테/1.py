import itertools
def solution(student, k):
    answer = -1
    lst = [[] for _ in range(len(student))]
    cnt = 0
    for i in range(len(student)):
        for j in range(len(student)):
            if student[i] == 0:
                lst[i].append(student[j])
                if lst[i].count(1) == k:
                    break

            elif student[i] == 1:
                lst[i].append(student[j])
    print(lst)
    return answer
solution([0, 1, 0, 0, 1, 1, 0],2)