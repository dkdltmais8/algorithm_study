def solution(sticker):
    answer = 0
    n = len(sticker)
    if n == 1:
        return sticker[0]
    #dp1 = 첫 스티커를 선택
    #dp2 = 두번째 스티커부터 선택
    dp1 = [0]*n
    dp2 = [0]*n
    dp1[0] = sticker[0]
    dp1[1] = sticker[0]
    #첫번째 스티커를 선택했으므로 마지막 스티커는 선택 못함
    for i in range(2,n-1):
        #전 칸의 값을 가져갈지 전전칸의 값에 현재 스티커 값을 더할 것인지 결정
        dp1[i] = max(dp1[i-2]+sticker[i],dp1[i-1])
    ans1 = max(dp1)
    dp2[1] = sticker[1]
    for i in range(2,n):
        dp2[i] = max(dp2[i-2]+sticker[i],dp2[i-1])
    ans2 = max(dp2)
    answer = max(ans1,ans2)
    return answer
solution([14, 6, 5, 11, 3, 9, 2, 10])
solution([99])
solution([95,100])