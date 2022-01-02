def solution(n, k):
    answer = []
    arr = [i for i in range(1,n+1)]
    dp = [1,1,2]
    for i in range(3,21):
        dp.append(dp[i-1]*i)
    while n>0:
        mok = (k-1)//dp[n-1]
        answer.append(arr[mok])
        arr.pop(mok)
        k = k% dp[n-1]
        n-= 1
    return answer
solution(3,5)