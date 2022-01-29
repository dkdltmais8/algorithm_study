from copy import deepcopy
answer = [0,0]
def check(arr):
    now = arr[0][0]
    for r in range(len(arr)):
        for c in range(len(arr)):
            if arr[r][c] != now:
                return False
    else:
        return True
def solution(arr):
    global answer
    if check(arr):
        if arr[0][0] == 1:
            answer[1] += 1
        else:
            answer[0] += 1
    else:
        n = len(arr)
        if n == 1:
            if arr[0][0] == 1:
                answer[1] += 1
                return
            else:
                answer[0] += 1
                return
        else:
            s1=[[] for _ in range(n//2)]
            s2=[[] for _ in range(n//2)]
            s3=[[] for _ in range(n//2)]
            s4=[[] for _ in range(n//2)]
            for i in range(n):
                for j in range(n):
                    if i<n//2 and j<n//2:
                        s1[i].append(arr[i][j])
                    elif i<n//2 and j>=n//2:
                        s2[i].append(arr[i][j])
                    elif i>=n//2 and j<n//2:
                        s3[i-n//2].append(arr[i][j])
                    else:
                        s4[i-n//2].append(arr[i][j])
            solution(s1)
            solution(s2)
            solution(s3)
            solution(s4)
    return answer
print(answer)
#S내부에 모든 수가 같으면 하나의 수로 압축
#아니라면 s를 4개의 정사각형으로 나누고 다시 반복
solution([[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]]	)
print(answer)
solution([[1,1,1,1,1,1,1,1],[0,1,1,1,1,1,1,1],[0,0,0,0,1,1,1,1],[0,1,0,0,1,1,1,1],[0,0,0,0,0,0,1,1],[0,0,0,0,0,0,0,1],[0,0,0,0,1,0,0,1],[0,0,0,0,1,1,1,1]])
print(answer)