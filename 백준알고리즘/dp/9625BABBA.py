n = int(input())
cnt = 0
arr2 = [0,1]
for i in range(2, n + 1):
    arr2.append(arr2[i - 1] + arr2[i - 2])
print(arr2[n-1],arr2[n])
