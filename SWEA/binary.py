binary_code = {'0001101': 0, '0011001': 1, '0010011': 2, '0111101': 3, '0100011': 4,
               '0110001': 5, '0101111': 6, '0111011': 7, '0110111': 8, '0001011': 9}

for tc in range(int(input())):
    N, M = map(int, input().split())
    array = [input() for _ in range(N)]
    ans = list()
    for sero in range(N):
        for garo in range(M-1,-1,-1):
            if array[sero][garo] == '1':
                ans = array[sero][garo - 55:garo + 1]
    result = []
    start = 0
    end = 6
    for _ in range(8):
        result.append(binary_code.get(ans[start:end+1]))
        start += 7
        end += 7
    value = (result[0] + result[2] + result[4] + result[6])*3 + (result[1]+result[3]+result[5]) + result[7]
    if value % 10 == 0:
        print(f"#{tc+1} {sum(result)}")
