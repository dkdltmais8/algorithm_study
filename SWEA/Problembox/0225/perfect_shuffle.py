T = int(input())
for tc in range(1, T+1):
    n = int(input())
    str1 = list(map(str, input().split()))
    if n % 2 == 0:
        str2 = str1[0 : n // 2]
        str3 = str1[n // 2 : n]
    else:
        str2 = str1[0:(n//2)+1]
        str3 = str1[(n//2)+1: n]+['']

    print("#{}".format(tc), end=' ')
    if n % 2 == 0:
        for i in range(n//2):
            print(str2[i],end=' ')
            print(str3[i],end=' ')
        print()
    else:
        for i in range((n // 2)+1):
            print(str2[i],end=' ')
            print(str3[i],end = ' ')
        print()