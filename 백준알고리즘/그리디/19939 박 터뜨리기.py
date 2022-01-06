n, k = map(int,input().split())
tot = k*(k+1)//2
#최솟값인 tot 보다 n이 작으면 불가능
if n<tot:
    print(-1)
#n이 최솟값인 tot 보다 크고 다 채우고 남은 공을 k개에 똑같이 나눌 수 있으면
#최다 - 최빈은 변하지 않는다
elif n>=tot and (n-tot)%k==0:
    print(k-1)
#n이 최솟값인 tot 보다 크고 다 채우고 남은 공을 k개에 똑같이 나눌 수 없다면
#최다 - 최빈은 차이가 1 늘어난다.
else:
    print(k)
