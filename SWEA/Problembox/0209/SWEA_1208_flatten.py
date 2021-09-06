import sys
sys.stdin = open('flatten.txt' , 'r')

def my_max(a):
    max_num = a[0]
    for i in range(len(a)):
        if a[i] > max_num:
            max_num = a[i]
    return max_num

def my_min(a):
    min_num = a[0]
    for i in range(len(a)):
        if a[i] < min_num:
            min_num = a[i]
    return min_num
def idx_max_b():
    max_value = -1
    max_idx = -1
    for i in range(len(box_num)):
        if box_num[i] > max_value:
            max_value = box_num[i]
            max_idx = i
    return max_idx
def idx_min_b():
    min_value = 101
    min_idx = -1
    for i in range(len(box_num)):
        if box_num[i] < min_value:
            min_value = box_num[i]
            min_idx = i
    return min_idx

for i in range(1,11):
    dump = int(input())
    box_num = list(map(int,input().split()))
    for j in range(dump):
        box_num[idx_max_b()] -= 1
        box_num[idx_min_b()] += 1
    print(f"#{i} {box_num[idx_max_b()] - box_num[idx_min_b()]}")
