n= int(input())
arr = list(map(int,input().split()))
#벌집이 가운데 있을 때
ans1 = sum(arr)-arr[0]-arr[-1]+max(arr[1:n-1])
#벌집이 오른쪽에 있을 때
l = ll= sum(arr)-arr[0]
il,ir = 0,0
for i in range(1,n-1):
    #벌이 있다면 두 벌이 사용을 못하기 때문에
    ll -= 2*arr[i]
    #두 벌이 사용못한 값이 합 중에서 제일 크다면 그곳을 제외하면 된다(il에 다른 벌의 최대 값이 들어가있음)
    if il<ll:
        il = ll
    #한 벌만 사용한다는 가정을 만들어줌
    ll += arr[i]
r = rr = sum(arr)-arr[-1]
#오른쪽도 똑같이 진행
for i in range(n-2,-1,-1):
    rr -= 2*arr[i]
    if ir<rr:
        ir = rr
    rr += arr[i]
#가운데, 양쪽 끝인 경우를 다 구해서 제일 큰 값을 출력
print(max(ans1,il+l,ir+r))