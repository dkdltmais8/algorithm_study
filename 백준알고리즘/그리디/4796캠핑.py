cnt = 0
while 1:
    cnt += 1
    l,p,v = map(int,input().split())
    if l == 0 and p == 0 and v == 0:
        break
    else:
        mok = v//p
        nam = v-(mok*p)
        if nam >l:
            print(f"Case {cnt}: {mok*l + l}")
        else:
            print(f"Case {cnt}: {mok*l + nam}")