n = int(input())
A = list(map(int,input().split()))
s = int(input())
for i in range(n):
    j = n
    while s>0:
        #현재 위치가 구간 중에서 제일 큰 값이면 나가서 for문 다음 인덱스로 이동(j를 계속 줄여나감)
        if i == A.index(max(A[i:j])):
            break
        #아니라면 교환을 해야함
        else:
            #지금 값을 최대값으로 바꿀 수 있을만큼 기회가 남아있는지 체크
            if A.index(max(A[i:j]))-i<=s:
                #최대값의 위치 찾기
                idx = A.index(max(A[i:j]))
                # 지금 위치에서 최대값 위치 차이만큼 기회를 감소시킴
                s -= idx-i
                for k in range(idx,i,-1):
                    A[k],A[k-1] = A[k-1],A[k]
            #최대값 인덱스와 바꿀 수 없는 경우 범위를 줄여나가면서 남은 기회 안에서 옮길 수 있는 최대값을 찾음
            else:
                j-=1
print(*A)