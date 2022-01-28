from collections import deque
def solution(skill, skill_trees):
    answer = 0
    for i in skill_trees:
        lst = deque(skill)
        for j in i:
            if j in skill:
                if j != lst.popleft():
                    break
        else:
            answer += 1
    # print(answer)
    return answer
solution("CBD",	["BACDE", "CBADF", "AECB", "BDA"])