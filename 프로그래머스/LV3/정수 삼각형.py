def solution(triangle):
    answer = 0
    #bottom-up 방식으로 dp 채울 초석
    dp = [triangle[0]]
    #전체 triangle을 돌기
    for idx,val in enumerate(triangle):
        #한 val에서 사용할 list
        lst = []
        #처음은 dp에 있으니까 넘김
        if idx == 0:
            continue
        #마지막 index 검사할 때 사용할 변수
        end = len(val)-1
        #각 리스트 안에서 반복하기
        for jdx,num in enumerate(val):
            #현재 jdx가 0이면 idx-1에서 0 인덱스 값만 적용되므로 이렇게 설정
            if jdx == 0:
                lst.append(dp[idx-1][0]+num)
            # 현재 jdx가 끝이면 idx-1에서도 마지막 인덱스 값만 적용되므로 이렇게 설정
            elif jdx == end:
                lst.append(dp[idx-1][end-1]+num)
            # 그 외의 경우에는 양 쪽의 값중에 더 큰값과 현재의 값을 더해서 저장
            else:
                lst.append(max(dp[idx-1][jdx],dp[idx-1][jdx-1])+num)
        #각 리스트에서 추가가 끝나면 dp에 행별로 합쳐줌
        dp.append(lst)
    # print(dp)
    #마지막 행에서 제일 큰 값을 출력
    answer = max(dp[-1])
    return answer
solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]])