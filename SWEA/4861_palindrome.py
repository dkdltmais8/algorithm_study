T = int(input())
for tc in range(1, T+1):
    n, m = map(int,input().split())
    rev = ''
    ans = []
    string = [input() for _ in range(n)]
    if n == m:
        for i in range(n):
            if string[i] == string[i][::-1]:
                print("#{} {}".format(tc,string[i]))
                break
        for r in range(n):
            for c in range(n):
                rev += string[c][r]
            ans.append(rev)
            rev = ''
        for i in range(n):
            if ans[i] == ans[i][::-1]:
                print("#{} {}".format(tc,ans[i]))
    else:
        for i in range(n):
            for j in range(n-m+1):
                if string[i][j:j+m] == string[i][j:j+m][::-1]:
                    print("#{} {}".format(tc,string[i][j:j+m]))

        for r in range(n):
            for c in range(n):
                rev += string[c][r]
            ans.append(rev)
            rev = ''
        for i in range(n):
            for j in range(n-m+1):
                if ans[i][j:j + m] == ans[i][j:j + m][::-1]:
                    print("#{} {}".format(tc,ans[i][j:j + m]))

