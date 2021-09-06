a = int(input())
b = int(input())
total = int(0)
i = int(0)
result = int(0)
while int(b) > 0:
    total = (a*(b%10))
    b //= 10
    print(total)
    result += total *(10**i)
    i += 1
    if b ==0:
        break
print(result)
    
