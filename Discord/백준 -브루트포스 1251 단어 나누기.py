a = input()
lst = []
for i in range(1,len(a)-1):
    for j in range(i+1,len(a)):
        lst.append(a[:i][::-1]+a[i:j][::-1]+a[j:][::-1])
print(sorted(lst)[0])