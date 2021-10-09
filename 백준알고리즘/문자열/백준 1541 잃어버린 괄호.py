# -가 한번 나온 후에 다음 -가 나오기 전까지는 묶어야 제일 큰 -값을 구할 수 있으므로 -로 묶음
p = input().split('-')
#수의 합들을 보관할 수 있는 리스트
num = []
# -기준으로 나누어진 문자열을 돌면서
for i in p:
    cnt = 0
    # +가 중간에 있다면 나누어서 합을 구해줌
    s = i.split('+')
    for j in s:
        cnt += int(j)
    # 한번의 마이너스안에 최대한 많은 수를 넣어 리스트에 저장
    num.append(cnt)
# 제일 앞에는 -가 올 수 없으므로 첫번째 인덱스의 수에서 나머지 인덱스의 수들을 빼면 된다.
n = num[0]
for i in range(1,len(num)):
    n -= num[i]
print(n)
# 문자열은 split()만 잘써도 웬만큼 한다.