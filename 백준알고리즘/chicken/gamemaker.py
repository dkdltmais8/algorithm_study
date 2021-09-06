T = int(input())
point = []
cnt = 0
for _ in range(T):
    num = int(input())
    point.append(num)
for i in range(T-1, 0, -1):
    if point[i] <= point[i-1]:
        cnt += (point[i-1]-point[i] + 1)
        point[i-1] = point[i] - 1
print(cnt)