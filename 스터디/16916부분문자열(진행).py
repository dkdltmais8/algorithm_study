def make_pi(p):
    i = 0
    for j in range(1,len(p)):
        while i > 0 and p[i] != p[j]:
            i = pi[i-1]
        if p[i] == p[j]:
            i += 1
            pi[j] = i

def kmp(s,p):
    make_pi(p)
    i = 0
    for j in range(len(s)):
        while i>0 and s[j] != p[i]:
            i = pi[i-1]
        if s[j] ==p[i]:
            if i == len(p)-1:
                return True
            else:
                i += 1
    return False

s = input()
p = input()
pi = [0 for _ in range(len(p))]
if kmp(s,p):
    print(1)
else:
    print(0)
print(pi)