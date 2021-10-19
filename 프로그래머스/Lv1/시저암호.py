def solution(s, n):
    answer = ''
    for i in s:
        if i == ' ':
            answer += ' '
        if 90>=ord(i)>=65:
            if ord(i)+n > 90:
                answer += chr(ord(i)+n-26)
            else:
                answer += chr(ord(i)+n)
        elif 122 >= ord(i) >= 97:
            if ord(i)+n > 122:
                answer += chr(ord(i)+n-26)
            else:
                answer += chr(ord(i)+n)
    # print(ord('Z'),ord('A'),ord('z'),ord('a'))
    return answer
solution("AB",1)
solution("z",1)
solution("a B z",4)