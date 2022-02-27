import heapq,sys
input=sys.stdin.readline
n = int(input())
arr = []
for i in range(n):
    arr.append(list(map(int,input().split())))
#시작하는 순서대로 바꾸기
arr.sort(key=lambda x:x[0])
#현재 방상태를 알기 위한 리스트
now = []
#첫번째 강의의 끝나는 시간 저장
heapq.heappush(now,arr[0][1])
for i in range(1,n):
    #새로운 강의실을 열어야 한다면 그 강의의 끝나는 시간 저장
    if now[0]>arr[i][0]:
        heapq.heappush(now,arr[i][1])
    #강의실을 새로 열 필요가 없다면 기존의 강의 없애고 새로운 강의로 갱신
    else:
        heapq.heappop(now)
        heapq.heappush(now,arr[i][1])
#남아있는 강의 개수만 체크해주면 실제로 필요한 강의실의 개수를 알 수 있다.
print(len(now))