C= int(input())
li_avg = []
for i in range(C):
    li = list(map(int,input().split(' ')))
    avg = sum(li[1:])/li[0]
    cnt = 0
    for j in li[1:]:
        if j > avg:
            cnt += 1
    A = cnt/li[0]
    li_avg.append(A)
for i in li_avg:
    print("{0:.3f}%" .format(100*i))