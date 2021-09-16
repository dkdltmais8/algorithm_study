def sensor():
    # 센서사이의 거리를 확인하기 위해 편하게 바끔
    arr.sort()
    ans = []
    #n이 1일 때 이거나 혹은 모든 n을 집중국으로 만들어 거리차가 없을 때
    if k>=n:
        return 0
    # 거리순으로 정렬된 센서의 차를 구함
    for i in range(1, n):
        ans.append(arr[i] - arr[i - 1])
    # print(ans)
    # 제일 거리차가 큰 센서를 나누기 위해서 정렬
    ans.sort()
    # k개의 집중국을 만드려면 k-1만큼 잘라주면 됨
    for i in range(k - 1):
        # 거리차가 큰 센서가  제일 뒤에 있으므로 뒤에서부터 자름
        ans.pop()
    return sum(ans)
n = int(input())
k = int(input())
arr = list(map(int,input().split()))
res = sensor()
print(res)
