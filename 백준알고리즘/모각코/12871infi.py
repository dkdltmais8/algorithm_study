def check(s,t):
    if len(s) > len(t):
        s,t = t,s
    if s*(len(t)) == t*(len(s)):
        return 1
    else:
        return 0
s = input()
t = input()
print(check(s,t))
