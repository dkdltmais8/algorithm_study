import sys
input = sys.stdin.readline
def check_palin(p):
    if p == p[::-1]:
        return True
    return False
def check_prime(num):
    for i in range(2,int(num**0.5)+1):
        if num%i == 0:
            return False
    return True
n,m = map(int,input().split())
if m>10000000:
    m = 10000000
ans = [i for i in range(n,m+1) if check_palin(str(i))]
ans = [i for i in ans if check_prime(i)]
for i in ans:
    print(i)
print(-1)