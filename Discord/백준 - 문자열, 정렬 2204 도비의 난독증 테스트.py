while 1:
    n = int(input())
    arr = []
    if n ==0:
        break
    for i in range(n):
        ex = input()
        arr.extend([[ex.lower(),ex]])
    arr.sort(key=lambda x:x[0])
    print(arr[0][1])
