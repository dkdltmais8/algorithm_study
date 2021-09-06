from itertools import combinations
while 1:
    arr= list(map(int,input().split()))
    if arr[0] == 0:
        break
    else:
        del arr[0]
    ans = list(combinations(arr,6))
    for i in ans:
        for j in i:
            print(j,end=" ")
        print()
    print()