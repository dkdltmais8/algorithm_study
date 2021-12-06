def solution(routes):
    answer = 0
    lst = []
    routes.sort(key=lambda x:x[1])
    print(routes)
    lst.append(routes[0][1])
    routes.pop(0)
    i = 0
    while len(routes)>=1:
        if routes[0][0]<= lst[i] <= routes[0][1]:
            routes.pop(0)
        else:
            i+=1
            lst.append(routes[0][1])
            routes.pop(0)
    print(routes)
    print(lst)
    answer = len(lst)
    return answer
solution([[-20,-15], [-14,-5], [-18,-13], [-5,-3]]	)