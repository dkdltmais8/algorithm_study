s = input()
flag = True
idx1 = s.find("U")
if idx1 == -1:
    flag = False
idx2 = s[idx1+1:].find("C")
if idx2 == -1:
    flag = False
idx3 = s[idx1+idx2+1:].find("P")
if idx3 == -1:
    flag = False
idx4 = s[idx1+idx2+idx3+1:].find("C")
if idx4 == -1:
    flag = False
if not flag:
    print("I hate UCPC")
else:
    print("I love UCPC")

