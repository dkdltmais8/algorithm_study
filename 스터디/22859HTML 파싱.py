##<가 나오면 어떤 태그인지 검사하고 div이면 a ='b' 의 형태를 a : b로 바꾸고
##  p태그이면 p태그 끝나기 전까지 다른 태그 있으면 지우고 그 사이에 있는 문자열 출력
#####################################시간 초과#########################################################
str1 = input()
answer = ''

for idx in range(len(str1)):
    if str1[idx:idx+3] == '</m':
        break
    if str1[idx:idx+5] == '<div ':
        idx1 = str1.find('"',idx)
        idx2 = str1.find('"',idx1+1)
        answer += 'title : ' + str1[idx1+1:idx2]
        print(answer)
        answer = ''
    elif str1[idx:idx+3] == '<p>':
        idx3 =str1.find('</p>',idx+3)
        while str1.find('<',idx+3,idx3) != -1:
            idx3 = str1.find('</p>', idx + 3)
            bad1 = str1.find('<',idx+3,idx3)
            bad2 = str1.find('>',bad1)
            str1 = str1[:bad1]+str1[bad2+1:]
            # str1 = str1[bad1:bad2+1].replace(str1[bad1:bad2+1],' ')
            # print(str1)
        answer += str1[idx+3:idx3]
        print(answer)
        answer = ''


###############################ModuleNotFound###################################################################
# from bs4 import BeautifulSoup
# str1 = input()
# soup = BeautifulSoup(str1, 'html.parser')
# a= soup.find_all('div')
# print(a)
# for i in a:
#     print("title : {}".format(i['title']))
#     for j in i:
#         print("{}".format(j.text))


##########################종우님 정답#################################
# string = input()
# divs = string.split('<div title="')
# for i in range(1, len(divs)):
#     div = divs[i]
#     p_list = div.split('<p>')
#     title = p_list.pop(0)
#     title = title[:-2]
#     print('title :', title)
#     # p태그들
#     for ps in p_list:
#         sentence = ''
#         j = 0
#         while j < len(ps):
#             # 태그기호는 다 제거 '<' 나오면 '>' 나올 때까지 스킵
#             if ps[j] == '<':
#                 for k in range(j+1, len(ps)):
#                     if ps[k] == '>':
#                         j = k
#                         break
#             else:
#                 sentence += ps[j]
#             j += 1
#         # 띄어쓰기 한칸씩만 만들어주기
#         result = sentence.split()
#         result = ' '.join(result)
#         print(result)