from collections import defaultdict
def solution(arrows):
    answer = 0
    visit = defaultdict(list)
    x,y = 0,0
    dx,dy = [0,1,1,1,0,-1,-1,-1],[1,1,0,-1,-1,-1,0,1]

    for arrow in arrows:
        # 대각선 판별을 위해 2씩
        for _ in range(2):
            nx = x + dx[arrow]
            ny = y + dy[arrow]
            # 방문했던 점이지만 경로가 겹치지 않는 경우, 방+1
            # 기존의 점은 없지만 도착하는 점이 방문 체크가 되어 있다면 정점은 중복, 간선은 처음이라는 것을 알 수 있다.
            if (nx,ny) in visit and (x,y) not in visit[(nx,ny)]:
                answer += 1
                visit[(x,y)].append((nx,ny))
                visit[(nx,ny)].append((x,y))
            # 방문하지 않았던 경우에는 그냥 추가해주기
            elif (nx,ny) not in visit:
                visit[(x,y)].append((nx,ny))
                visit[(nx,ny)].append((x,y))
            # 이동
            x,y = nx, ny
    return answer

def solution(arrows):
    answer = 0
    visit = [(0,0)]
    edge = []
    dx, dy = [0, 1, 1, 1, 0, -1, -1, -1], [1, 1, 0, -1, -1, -1, 0, 1]
    for arrow in arrows:
        for _ in range(2):
            x,y = visit[-1]
            nx,ny = dx[arrow],dy[arrow]
            visit.append((x+nx,y+ny))
            if visit[-2]<visit[-1]:
                edge.append((visit[-2],visit[-1]))
            else:
                edge.append((visit[-1],visit[-2]))
    edges = len(edge) - len(set(edge))
    nodes = len(visit) - len(set(visit))
    answer = nodes-edges
    return answer
solution([6, 6, 6, 4, 4, 4, 2, 2, 2, 0, 0, 0, 1, 6, 5, 5, 3, 6, 0]	)