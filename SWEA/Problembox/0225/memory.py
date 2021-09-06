T = int(input())
for tc in range(1, T+1):
    memory = list(input())
    n = len(memory)
    bit = ['0']*n
    cnt = 0
    i = 0
    while i < n:
        if bit[i] != memory[i]:
            if bit[i] == '0':
                for j in range(i,n):
                    bit[j] = '1'
                cnt += 1
            elif bit[i] == '1':
                for j in range(i,n):
                    bit[j] = '0'
                cnt += 1
        i += 1


    print("#{} {}".format(tc,cnt))


