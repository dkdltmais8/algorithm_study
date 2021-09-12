import heapq
def solution(info, edges):
    answer = 0
    lst = [[] for _ in range(len(info)+1)]
    for i in range(len(edges)):
        v,e = edges[i][0],edges[i][1]
        lst[v].append(e)
    for i in lst:
        for j in i:

    print(lst)
    return answer
solution([0,0,1,1,1,0,1,0,1,0,1,1],[[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]])