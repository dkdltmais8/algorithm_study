import itertools
def ans():
    res = []
    for i in list(itertools.combinations(arr,n)):
        vowelcnt = consonantcnt = 0
        for j in i:
            if j in vowels:
                vowelcnt += 1
            else:
                consonantcnt += 1
        if vowelcnt > 0 and consonantcnt > 1:
            res.append(''.join(i))
    return res
n,m = map(int,input().split())
arr = sorted(input().split())
vowels = set(['a','e','i','o','u'])
for i in ans():
    print(i)