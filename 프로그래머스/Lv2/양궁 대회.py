from copy import deepcopy
d, answer = 0,[]
def check(s1,s2,cnt,idx,arr,n,info):
    global d,answer
    #화살 개수가 n보다 크면 돌아감
    if cnt>n:
        return
    #10점 화살까지 전부 계산을 끝냈다면 차이를 구해서 최대 차이인지 확인
    #최대 차이이면 제일 마지막에 남은 화살 개수를 더해줌
    if idx>10:
        diff = s2-s1
        if diff>d:
            d = diff
            arr[10] = n-cnt
            answer = arr
        return
    #아직 화살을 쏠 수 있다면 현재 위치에서 어피치보다 1발 더 손 상태로 바꿔주고
    #점수 추가, 횟수 추가, idx 이동을 시킨 상태로 재귀
    if cnt < n:
        lst = deepcopy(arr)
        lst[10-idx] = info[10-idx]+1
        check(s1,s2+idx,cnt+info[10-idx]+1,idx+1,lst,n,info)
    lst2 = deepcopy(arr)
    #어피치의 점수 구하기
    if info[10-idx]>0:
        check(s1+idx,s2,cnt,idx+1,lst2,n,info)
    #어피치가 0점 쏜 과녁은 넘어가기
    else:
        check(s1,s2,cnt,idx+1,lst2,n,info)
def solution(n, info):
    global answer
    #화살 개수가 처음부터 10점에 전부 있으면 절대 이길 수 없음
    if n == info[0]:
        return [-1]
    #최종 점수가 같으면 라이언이 짐
    #어피치, 라이언이 같은 수를 맞췄으면 어피치가 점수 가져감(어피치보다 1발 더 쏴야함)
    #뒤에서부터 점수를 채우고 총합을 구해서 총합과 리스트를 갖고 있고
    #높은 점수쪽으로 진행하면서 총합이 커지면 리스트를 바꿔주고
    #총합이 같으면 리스트에 추가를 해준다.
    ryan = [0]*11
    check(0,0,0,0,ryan,n,info)
    return answer if answer else [-1]
solution(5,[2,1,1,1,0,0,0,0,0,0,0])