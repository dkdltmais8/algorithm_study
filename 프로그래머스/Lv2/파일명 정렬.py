def solution(files):
    answer = []

    for i in files:
        head = ""
        num = ""
        tail = ""
        isnum = 0
        for j in range(len(i)):
            if i[j].isdigit():
                num+= i[j]
                isnum = 1
            elif  not isnum:
                head += i[j]
            else:
                tail = i[j:]
                break
        answer.append([head,num,tail])
    answer.sort(key= lambda x: (x[0].lower(),int(x[1])))
    return [''.join(ans) for ans in answer]