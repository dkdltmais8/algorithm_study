import itertools
n = int(input())
ans = [1,5,10,50]
res = list(itertools.combinations_with_replacement(ans,n))
no =[]
for i in res:
    no.append(sum(i))
no = list(set(no))

print(len(no))