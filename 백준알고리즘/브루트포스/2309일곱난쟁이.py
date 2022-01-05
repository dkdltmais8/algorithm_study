arr = [int(input()) for i in range(9)]
arr.sort()
tot = sum(arr)
for i in range(9):
    for j in range(i+1,9):
        if tot - arr[i]-arr[j] == 100:
            del arr[i]
            del arr[j-1]
            break
    if len(arr)==7:
        break
for i in arr:
    print(i)