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
                print(num)
                isnum = 1
            elif  not isnum:
                head += i[j]
                print(head)
            else:
                tail = i[j:]
                print(tail)
                break
        answer.append([head,num,tail])
    answer.sort(key= lambda x: (x[0].lower(),int(x[1])))
    print(answer)
    return [''.join(ans) for ans in answer]
solution(["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"])
solution(["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"])