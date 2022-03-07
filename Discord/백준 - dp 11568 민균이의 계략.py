from bisect import bisect_left
n = int(input())
arr = list(map(int,input().split()))
answer = [0]
for i in arr:
    if i>answer[-1]:
        answer.append(i)
    else:
        answer[bisect_left(answer,i)] = i
print(len(answer)-1)
print(answer)