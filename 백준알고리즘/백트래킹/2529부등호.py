def possible(idx,pre,cur):
    if icon[idx] == '<' and pre < cur:
        return True
    if icon[idx]== '>' and pre > cur:
        return True
    return False

def find_max(num, idx, pre):
    global max_arr
    if idx == 0:
        num = [pre]
    if idx >= n :
        max_arr = num
        return
    for i in range(9,-1,-1):
        if not max_arr and i not in num:
            if possible(idx,pre,i):
                find_max(num+[i],idx+1,i)
def find_min(num, idx, pre):
    global min_arr
    if idx == 0:
        num = [pre]
    if idx >= n :
        min_arr = num
        return
    for i in range(10):
        if not min_arr and i not in num:
            if possible(idx,pre,i):
                find_min(num+[i],idx+1,i)


n = int(input())
icon = list(map(str,input().split()))
max_arr = []
min_arr = []
for i in range(10):
    if not max_arr:
        find_max([],0,9-i)
    if not min_arr:
        find_min([],0,i)
for i in max_arr:
    print(i,end='')
print()
for i in min_arr:
    print(i,end='')