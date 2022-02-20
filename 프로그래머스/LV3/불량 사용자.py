from collections import defaultdict
def solution(user_id, banned_id):
    answer = 0
    def check(s1):
        nonlocal dic
        for s2 in user_id:
            flag = False
            if len(s1) != len(s2):
                continue
            for i in range(len(s1)):
                if s1[i] != s2[i]:
                    if s1[i] == '*':
                        continue
                    else:
                        flag = True
                        break
            if flag:
                continue
            dic[s1] += 1
    dic = defaultdict(int)
    for i in banned_id:
        if i not in dic:
            check(i)
    print(dic)
    return answer

###키 카운트해서 개수 체크하기
###벨류 중복 체크해서 중복 있는 키랑 카운트 합치고 벨류 중복값 빼고 카운트
solution(["frodo", "fradi", "crodo", "abc123", "frodoc"],["fr*d*", "abc1**"])
solution(["frodo", "fradi", "crodo", "abc123", "frodoc"],["*rodo", "*rodo", "******"])
solution(["frodo", "fradi", "crodo", "abc123", "frodoc"],["fr*d*", "*rodo", "******", "******"])