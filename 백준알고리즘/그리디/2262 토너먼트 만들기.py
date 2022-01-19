n = int(input())
lst = [600]+list(map(int,input().split()))+[600]
tot = 0
while n>= 2:
    i = lst.index(n)
    tot += min(abs(lst[i]-lst[i-1]),abs(lst[i]-lst[i+1]))
    lst.remove(n)
    n-=1
print(tot)
