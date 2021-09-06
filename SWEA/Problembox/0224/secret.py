def check():
    global str1, n
    for _ in range(n-1):
        for i in range(n-1,0,-1):
            if str1[i] == str1[i-1]:
                str1 = str1[0:i-1] + str1[i+1: n]
                n -= 2
                break

    return str1

for tc in range(1, 11):

    n, str1 = map(str, input().split())
    n = int(n)
    print("#{} {}".format(tc, check()))
