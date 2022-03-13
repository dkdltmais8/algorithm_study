s = input()
zero = []
one = []
for i in range(len(s)-1):
    if s[i] != s[i+1]:
        if s[i] == '0':
            zero.append(1)
        else:
            one.append(1)
print(max(len(zero),len(one)))
