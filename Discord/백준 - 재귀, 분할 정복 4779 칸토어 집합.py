def make(n,s):
    if n == 1:
        return s
    size = n//3
    return make(n//3,s[:size]) + s[size:size*2].replace('-',' ') + make(n//3,s[2*size:])
while 1:
    try:
        n = int(input())
        num = 3**n
        s = '-'*num
        ans = make(num,s)
        print(ans)
    except EOFError:
        break