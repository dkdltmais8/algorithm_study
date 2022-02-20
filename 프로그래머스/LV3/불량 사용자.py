from itertools import permutations
def solution(user_id, banned_id):
    def check(r,c):
        #길이가 다르면 *랑 상관없이 불가능
        if len(r) != len(c):
            return False
        else:
            for i,j in zip(r,c):
                # *이면 검사안하고 넘김
                if j == '*':
                    continue
                # 다르면 실패
                if i!=j:
                    return False
            #생성가능한 문자
            return True
    answer = []
    for i in permutations(user_id,len(banned_id)):
        cnt = 0
        for r,c in zip(i,banned_id):
            if check(r,c):
                #가능한 개수 증가
                cnt += 1
        #가능한 개수가 같으면 성공적인 검출
        if cnt == len(banned_id):
            #중복된 사용자는 불가능이기 때문에 중복검사
            if set(i) not in answer:
                answer.append(set(i))
    return len(answer)

solution(["frodo", "fradi", "crodo", "abc123", "frodoc"],["fr*d*", "abc1**"])
# solution(["frod, "fradi", "crodo", "abc123", "frodoc"],["fr*d*", "*rodo", "******", "******"])