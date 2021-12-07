def solution(lines):
    answer = 0
    time = []
    exe = []
    d = len(lines)
    for i in range(d):
        print(lines[i])
        # lines[i] = lines[i].split(':')
        lines[i]=lines[i].split(' ')
    for i in range(d):
        minus = lines[i][2].find('s')
        exe.append(lines[i][2][:minus])

    print(lines)
    print(exe)
    return answer
solution(["2016-09-15 01:00:04.001 2.0s","2016-09-15 01:00:07.000 2s"])