T = int(input())
for tc in range(1, T+1):
    card = list(input())
    deck = [[i for i in range(1,14)] for _ in range(4)]
    my_deck_s = []
    my_deck_d = []
    my_deck_h = []
    my_deck_c = []
    error = 0
    for i in range(0,len(card),3):
        if card[i] == "S":
            my_deck_s.append((int(card[i+1]+card[i+2])))
        elif card[i] == "D":
            my_deck_d.append(int(card[i+1]+card[i+2]))
        elif card[i] == "H":
            my_deck_h.append(int(card[i+1]+card[i+2]))
        elif card[i] == "C":
            my_deck_c.append(int(card[i+1]+card[i+2]))
    for i in range(len(my_deck_s)):
        if my_deck_s.count(my_deck_s[i]) >= 2:
            error = "ERROR"
            break
    for i in range(len(my_deck_d)):
        if my_deck_d.count(my_deck_d[i]) >= 2:
            error = "ERROR"
            break
    for i in range(len(my_deck_h)):
        if my_deck_h.count(my_deck_h[i]) >= 2:
            error = "ERROR"
            break
    for i in range(len(my_deck_c)):
        if my_deck_c.count(my_deck_c[i]) >= 2:
            error = "ERROR"
            break
    if error == "ERROR":
        print("#{} {}".format(tc, error))
    else:

        print("#{} {} {} {} {}".format(tc, 13-len(my_deck_s),13-len(my_deck_d),13-len(my_deck_h),13-len(my_deck_c)))
