T = int(input())
for tc in range(1, T+1):
    n, m = map(str, input().split())
    m = int(m)
    string = list(map(str,input().split()))
    example = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    cnt = [0]*10
    ans = []
    for i in range(len(string)):
        for j in range(len(example)):
            if string[i] == example[j]:
                cnt[j] += 1
    for i in range(len(example)):
        ans.append((example[i]+' ') * cnt[i])

    print('#{}'.format(tc))
    print(*ans)

