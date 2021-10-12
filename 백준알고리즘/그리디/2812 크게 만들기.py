n, m = map(int,input().split())
num = input()
Q = []
cnt = m
for i in range(n):
    while cnt > 0 and Q and Q[-1] < num[i]:
        Q.pop()
        cnt -= 1
    Q.append(num[i])
print(''.join(Q[:n-m]))