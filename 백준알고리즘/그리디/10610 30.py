n = int(input())
a = str(n)
a = sorted(a,reverse=True)
# print(a)
b= ''
for i in a:
    b+= i
if int(b)%30:
    print(-1)
else:
    print(int(b))
