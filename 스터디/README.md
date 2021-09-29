## 백준 - 17836 공주님을 구해라!

- BFS() => 최단 거리, 시간구하기
  - Q=>deque() 만들어서 while Q: 상태로 돌리기
  - Visit => 방문하면 1이 아닌 거리를 누적하는 형태로 사용
- 검을 구하지 않고 가는게 빠를 수도 있기 때문에 변수를 만들어 함수의 리턴값을 저장하고 이를 활용해서 해결한다.

## 백준 - 2212 센서 + 13164 행복유치원

- 그리디 알고리즘
- sort()와 append(), pop()을 활용하면 해결 가능



## 백준 - 17396 백도어

- 다익스트라 알고리즘 => 최단 경로 트리(가중치 이용)
  - 가중치의 합이 제일 적게 끝 노드에 도착
  - heapq, heappush, heappop 이용
  - 처음에 갈 수 있는 경로가 들어있는 List 만들어주기.(Graph)
  - 사용하는 함수만 다르고 BFS와 비슷함.(append 대신 heapq.heappush,      pop 대신 heapq.heappop)

## 백준 - 22859 HTML파싱

- split() 과 join, pop을 이용하면 가능
- 리스트로 만들어서 slice를 사용하면 시간초과 발생.



## 백준 - 16916 부분 문자열

- ﻿이런 문제가 왜 골드에 있을까 하고 브루트 포스로 시도했더니 바로 실패.

  브루트 포스가 시간 복잡도 O(N*M)이고, KMP 알고리즘으로 풀어야 O(N+M)이기 때문에 시간 초과.

  먼저 패턴에 접두사와 접미사가 같은 idx를 찾아 그때의 길이를 입력한 pi라는 리스트를 만들고

  이를 이용해 KMP 알고리즘을 사용한다.

  ![image.png](https://blogfiles.pstatic.net/MjAyMTA5MjlfMTU2/MDAxNjMyOTEzMDAwNTI4.ohVhqTVkBFYu7949HIMG3J3Ub4TW2GPunn0pOZqiNFQg.cIG__ofwdy4jAloi83byhbfSOr7DBI-2vvGcL8SkcgUg.PNG.dkdltmais9/image.png?type=w1)

  문자열과 패턴을 비교하며 진행하다가 다른 부분이 나오면 패턴의 인덱스(j)를 pi[j-1] 값으로 변경해 주고

  j = 1이 되고 j=2일 때 값이 같아서 통과한 건데 j=2와 j=0은 접두사와 접미사가 같기 때문에 j[1]과 문자열에서 현재 달랐던 b를 비교해서 같으면 거기서부터 이어서 체킹 한다.

  

  ﻿

