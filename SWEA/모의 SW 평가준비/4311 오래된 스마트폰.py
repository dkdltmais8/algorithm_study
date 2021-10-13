def check(num,cal,cnt,n):
    if cnt > touch_count:
        return -1
    if n>999 or n<0:
        return
    for i in num:
        


for tc in range(1, int(input())+1):
    touch_num,touch_cal,touch_count= map(int,input().split())
    num = list(map(int,input().split()))
    cal_lst = ['+','-','*','/']
    lst = list(map(int,input().split()))
    cal = []
    for i in lst:
        cal.append(cal_lst[i-1])
    ans = int(input())
    print(num,cal,ans,touch_count)

