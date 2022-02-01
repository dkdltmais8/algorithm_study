def solution(n, words):
    answer = []
    lst = []
    cycle,person = 1,1
    for i in range(len(words)):
        if i>0:
            if words[i-1][-1]!=words[i][0]:
                answer.append([person,cycle])
                break
        if words[i] in lst or len(words[i]) == 1:
            answer.append([person,cycle])
            break
        lst.append(words[i])
        if person == n:
            person = 0
            cycle += 1
        person += 1
    if answer == []:
        answer = [[0,0]]
    return answer[0]
#단어의 끝말과 다음 단어의 시작말이 다르면 탈락
#중복 단어 나오면 탈락
#탈락 없으면 0,0
solution(2, ['qwe', 'eqwe', 'eqwe'])
solution(2,['land', 'dream', 'mom', 'mom', 'ror'])
solution(2,["hello", "one", "even", "never", "now", "world", "draw"])
solution(3,["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"])
solution(5,["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure", "establish", "hang", "gather", "refer", "reference", "estimate", "executive"])