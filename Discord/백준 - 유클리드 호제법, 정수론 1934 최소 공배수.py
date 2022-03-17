def GCD(a,b):
    return GCD(b%a,a) if a else b
for _ in range(int(input())):
    n,m = map(int,input().split())
    print(m*n//GCD(n,m))
