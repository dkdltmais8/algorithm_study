n = int(input())
arr = [0] * 36
arr[0:4] = 1,1,2,5
for i in range(4,n+1):
    t = 0
    if i % 2:
        for j in range(i//2):
            t += 2*arr[j]*arr[i-j-1]
        arr[i] = t + arr[i//2]**2
    else:
        for j in range(i//2):
            t += 2*arr[j]*arr[i-j-1]
        arr[i] = t
print(arr[n])