def bfs(idx,num):
    global flag, ans
    if flag:
        return
    if idx == len(data):
        if num == max_num:
            flag = True
            ans = " ".join(map(str,arr))
            print(arr)
        return
    num1 = int(data[idx])
    if not visited[num1]:
        visited[num1] = 1
        arr[num] = num1
        print(arr)
        bfs(idx+1,num+1)
        visited[num1] = 0
    if idx < len(data)-1:
        num2 = int(data[idx:idx+2])
        if num2 < max_num+1 and not visited[num2]:
            visited[num2] = 1
            arr[num] = num2
            print(arr)
            bfs(idx+2,num+1)
            visited[num2] = 0
data = input()
if len(data) < 10:
    max_num = len(data)
else:
    max_num = 9 + (len(data)-9) // 2
visited = [0] * (max_num+1)
arr = [0]* (max_num)
flag = False
bfs(0,0)
print(ans)
print(arr)