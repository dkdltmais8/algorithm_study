T = int(input())
for tc in range(1, T+1):
    a = input()
    if a == a[::-1]:
        res = 1
    else:
        res = 0
    print("#{} {}".format(tc,res))