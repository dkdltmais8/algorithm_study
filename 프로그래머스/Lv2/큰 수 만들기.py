def solution(number, k):
    answer = ''
    Stack = []
    for num in number:
        while Stack and k>0 and int(Stack[-1])<int(num):
            Stack.pop()
            k-=1
        Stack.append(num)
    for i in Stack:
        answer+=i
    # print(Stack)
    print(answer)
    print(answer[:len(Stack)-k])
    return answer[:len(Stack)-k]
solution("1924",2)
solution("1231234",3)
solution("4177252841",4)
solution("111",2)