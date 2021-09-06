for tc in range(1, int(input()) + 1):
    N = int(input())
    # 버스노선정보 저장
    lines = []
    for i in range(N):
        lines.append(list(map(int, input().split())))

    #버스 노선개수 카운트 (정류장번호 -1에 빈도수 저장)
    count = [0]*5000
    for line in lines:
        for dis in range(line[0]-1, line[1]):
            count[dis] += 1

    #물어보는 정류장의 방문 횟수 출력
    P = int(input())
    print('#{}'.format(tc), end=' ')
    for bus_stop in range(P):
        C = int(input())
        print('{}'.format(count[C-1]), end=' ')
    print()