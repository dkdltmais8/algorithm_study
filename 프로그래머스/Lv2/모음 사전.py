from itertools import product
def solution(word):
    answer = 0
    p = ["A","E","I","O",'U']
    w = []
    for i in range(1,6):
       for j in product(p,repeat=i):
           l = ''.join(j)
           w.append(l)
    w.sort()
    answer = w.index(word)+1
    return answer
solution("AAAAE")

