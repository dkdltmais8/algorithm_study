import sys
sys.stdin = open('input.txt', 'r')
def my_max(a):
    max_value = a[0]
    for i in range(1,len(a)):
        if max_value < a[i]:
            max_value = a[i]
    return max_value

a=[1,2,3,6,5,4]

for i in range(1,11):
    N = int(input())
    result = list(map(int, input().split()))
    total = 0
    for idx in range(2, N-1):
        if result[idx] > result[idx + 1] and result[idx] > result[idx + 2] and result[idx] > result[idx - 1] and result[idx] > result[idx-2]:
            if my_max(result[idx-2:idx]) > my_max(result[idx+1:idx+3]):
                total += result[idx]-my_max(result[idx-2:idx])
            else:
                total += result[idx]-my_max(result[idx+1:idx+3])
    print("#{} {}" .format(i,total))