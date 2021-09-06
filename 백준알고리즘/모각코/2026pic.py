n,k,m = map(int,input().split())
#start가 0부터 시작이니까 m을 하나줄임
m -= 1
def search(n,k,m,start):
    cnt = 0
    while True:
        cnt += 1
        next_start = (start-1+k) % n
        #다음 스타트가 나이면 그 전의 사람이 나간것이기 때문에 start+k에서 -1을 해준다.
        if next_start ==  m:
            return cnt
        elif next_start < m:
            m -= 1
        else:
            pass
        n -= 1
        start = next_start
print(search(n, k, m, 0))