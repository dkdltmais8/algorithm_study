def factorial(n):
    tot = 1
    if n == 0:
        return 1
    for i in range(n,0,-1):
        tot *= i
    return tot
for tc in range(1,int(input())+1):
    w,e = map(int,input().split())
    ans = factorial(e)//(factorial(w)*factorial(e-w))
    print(ans)