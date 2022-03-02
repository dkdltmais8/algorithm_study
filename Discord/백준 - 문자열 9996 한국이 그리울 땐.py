n = int(input())
p = input().split('*')
s = len(p[0])
e = len(p[1])
for i in range(n):
    A = input()
    #앞이랑 뒤가 같고 서로 중복되지 않으면 합격
    if A[0:s] == p[0] and A[-e:] == p[1] and len(A)>=len(''.join(p)):
        print("DA")
    else:
        print("NE")