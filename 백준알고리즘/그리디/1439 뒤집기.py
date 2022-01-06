n = list(input())
zero = 0
one = 0
idx = 0
now =''
while idx<len(n):
    if n[idx] == '1' and now != '1':
        one += 1
    elif n[idx] == '0' and now != '0':
        zero += 1
    now = n[idx]
    idx += 1
print(min(one,zero))
