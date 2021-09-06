def factorial(n):
    if n == 1:
        return 1
    elif n >= 2:
        return n*factorial(n-1)
    elif n == 0:
        return 1
li = []
for i in range(int(input())):
    result = list(map(int, input().split()))
    n = result[0]
    r = result[1]
    combi = factorial(r)/(factorial(n)*factorial(r-n))
    li.append(combi)
for i in li:
    print(int(i))