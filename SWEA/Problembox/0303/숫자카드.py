from collections import deque
for tc in range(1, int(input())+1):
    card = [i for i in range(1,int(input())+1)]
    n = len(card)
    card = deque(card)
    while n > 1:
        card.popleft()
        if len(card) == 1:
            print("#{} {}".format(tc,*card))
            break
        card.append(card.popleft())
