for tc in range(1,int(input())+1):
    n = int(input())
    ans = []
    arr = list(map(int,input().split()))
    d = len(arr)
    for i in range(d):
        for j in range(d):
            for k in range(d):
                for l in range(d):

