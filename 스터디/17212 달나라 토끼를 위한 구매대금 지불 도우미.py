n = int(input())
if n>=8:
    money = [0,1,1,2,2,1,2,1]+[0]*(n-7)
    for i in range(8,n+1):
        money[i] = min(money[i-1]+1,money[i-2]+1,money[i-5]+1,money[i-7]+1)
    print(money[n])
else:
    money = [0, 1, 1, 2, 2, 1, 2, 1]
    print(money[n])