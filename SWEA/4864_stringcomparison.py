T = int(input())
for tc in range(1, T+1):
    a = input()
    b = input()
    if a in b:
        print("#{} 1" .format(tc))
    else:
        print("#{} 0" .format(tc))

