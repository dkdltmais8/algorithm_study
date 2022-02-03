from itertools import combinations
def solution(relation):
    answer = 0
    n = len(relation)
    d = len(relation[0])
    lst = []
    #후보키가 될 수 있는 인덱스 모든 조합
    for i in range(1,d+1):
        lst.extend(combinations(range(d),i))
    ans = []
    for i in lst:
        arr = [tuple([j[k] for k in i]) for j in relation]
        #유일성 검사
        if len(set(arr)) == n:
            flag = True
            #최소성 검사 ( 기존에 성공했던 것이 지금 성공한 것에 대한 부분집합이라면 지금 것은 최소가 아니기 때문에 x)
            for j in ans:
                if set(j).issubset(set(i)):
                    flag = False
                    break
            if flag:
                ans.append(i)
    answer = len(ans)
    return answer
solution([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]])