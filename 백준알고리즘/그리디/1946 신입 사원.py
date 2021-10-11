import sys
T = int(sys.stdin.readline().rstrip())
for tc in range(1,T+1):
    n = int(sys.stdin.readline().rstrip())
    scores = [list(map(int,sys.stdin.readline().rstrip().split())) for _ in range(n)]
    scores.sort()
    cnt = 1
    Pass = scores[0][1]
    for i in range(1,len(scores)):
        if Pass > scores[i][1]:
            cnt += 1
            Pass= scores[i][1]
    print('{}'.format(cnt))
