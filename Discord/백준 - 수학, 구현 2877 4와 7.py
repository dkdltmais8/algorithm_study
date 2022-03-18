def binary_search(s,e):
    global ans
    while s<=e:
        m = (s+e)//2
        if len(ans) == cnt:
            break
        if n<=m:
            ans+='4'
            e=m-1
        elif n>m:
            ans +='7'
            s = m+1

n = int(input())
ans = ""
#자릿수
cnt = 0
#범위
tot = 0
#자릿수에 따라 2**자릿수 => 그 자릿수에서 만들 수 있는 수의 개수
while 1:
    cnt+=1
    tot += 2**cnt
    if tot-2**cnt<= n <= tot:
        #범위
        s,e = (tot-2**cnt)+1,tot
        break
binary_search(s,e)
print(ans)

