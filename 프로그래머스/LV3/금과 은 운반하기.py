def solution(a, b, g, ss, w, t):
    #a,b = 필요한 금,은의 양
    #g,s = 각 도시에 있는 금,은의 양
    #w,t = 각 도시에서 이동하는 데 걸리는 시간(편도), 옮길 수 있는 광물의 양
    answer = float('inf')
    s,e = 0,10**9*10**5*4
    while s<=e :
        mid = (s+e)//2
        mg,ms,total = 0,0,0
        for i in range(len(g)):
            ng,ns,nw,nt = g[i],ss[i],w[i],t[i]
            #왕복인지 편도인지 구분
            if mid//nt%2 == 1:
                cnt = (mid//nt//2)+1
            else:
                cnt = mid//nt//2
            #옮길 수 있는 만큼 옮기기
            mg += ng if ng<nw*cnt else nw*cnt
            ms += ns if ns<nw*cnt else nw*cnt
            #둘을 옮긴 것이 한번에 옮길 수 있는 양을 넘지 않았는지 검사
            total += ns+ng if ns+ng<nw*cnt else nw*cnt
        #현재 금과 은이 최소 조건을 만족하고 전체의 양이 금과 은을 합친것보다 같거나 크면 성공
        if mg>=a and ms>=b and total>=a+b:
            answer = min(answer,mid)
            e = mid-1
        else:
            s = mid+1
    return answer
solution(10,10,[100],[100],[7],[10])
solution(90,500,[70,70,0],[0,0,500],[100,100,2],[4,8,1])