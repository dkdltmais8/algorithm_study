import sys
order_list = [0] * 10001
for i in range(int(sys.stdin.readline())):
    a= int(sys.stdin.readline())
    order_list[a] += 1 

for i in range(10001):
    if order_list[i] != 0:
        for j in range(order_list[i]):
            print(i)

