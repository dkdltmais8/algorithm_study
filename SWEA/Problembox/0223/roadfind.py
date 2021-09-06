
for tc in range(1, 11):
    T, E = map(int, input().split())
    G = [[] for _ in range(101)]
    visit = [0]*100
    ve_list = list(map(int,input().split()))
    for i in range(0, E * 2, 2):
        s = ve_list[i]
        e = ve_list[i+1]
        G[s].append(e)

    S = []
    v = 0
    # 1) 시작 정점 v를 결정하여 방문한다.
    visit[v] = 1;

    S.append(v)
    while S:  # 스택이 공백이 될 때까지 2)를 반복한다.
        # 2) 정점 v에 인접한 정점 중에서 방문하지 않은 정점 w를 찾는다.
        for w in G[v]:
            if visit[w] == 0:
                S.append(v)
                visit[w] = 1  # 정점 v를 스택에 push하고 정점 w를 방문한다.
                v = w  # 그리고 w를 v로 하여 다시 2)를 반복한다.
                break

        else:
            v = S.pop()  # 방문하지 않았을 때
    if visit[99] == 1:
        print("#{} 1".format(tc))
    else:
        print("#{} 0".format(tc))




