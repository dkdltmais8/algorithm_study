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

# Q라는 스택을 만들고 뺄 수 있는 기회가 남아있고 뒤의 숫자가 앞의 숫자보다
# 크며 스택 안에 원소가 존재한다면 값을 바꾸는 식으로 만들었다. 큰 수를 만들기 위해서는
# 제일 앞자리의 숫자가 가장 커야 하기 때문에 while 문으로 허용되는 횟수 내에서 제일 큰 값을 넣을 수 있도록 만들어준다.