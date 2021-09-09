def solution(new_id):
    answer = ''
    # 1
    new_id = new_id.lower()
    # 2
    for c in new_id:
        if c.isalpha() or c.isdigit() or c in ['-', '_', '.']:
            answer += c
    # 3
    while '..' in answer:
        answer = answer.replace('..', '.')
    # 4
    if answer[0] == '.':
        answer = answer[1:] if len(answer) > 1 else '.'
    if answer[-1] == '.':
        answer = answer[:-1]
    # 5
    if answer == '':
        answer = 'a'
    # 6
    if len(answer) > 15:
        answer = answer[:15]
        if answer[-1] == '.':
            answer = answer[:-1]
    # 7
    while len(answer) < 3:
        answer += answer[-1]
    return answer


#
# capitalize() => 문자열 맨 앞 문자만 대문자
# title() => 각 단어의 첫 문자를 대문자
# lower() => 소문자로 변경
# upper() => 대문자로 변경
# casefold() => 영어가 아닌 언어도 소문자로 변경 (위에는 다 영어만 적용)
# isalpha() => 알파벳인지 확인. 파이썬 3버전대는 한글도 가능. 띄어쓰기, 숫자 있으면 False
# isdigit() => 문자열의 구성이 숫자인지 확인. 특수문자, 글자 있으면 False
# isalnum() => isalpha() + isdigit()


# 정규화

# import re
#
# def solution(new_id):
#     st = new_id
#     st = st.lower()
#     st = re.sub('[^a-z0-9\-_.]', '', st)
#     st = re.sub('\.+', '.', st)
#     st = re.sub('^[.]|[.]$', '', st)
#     st = 'a' if len(st) == 0 else st[:15]
#     st = re.sub('^[.]|[.]$', '', st)
#     st = st if len(st) > 2 else st + "".join([st[-1] for i in range(3-len(st))])
#     return st
