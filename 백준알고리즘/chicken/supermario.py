point = [int(input()) for _ in range(10)]
tot1 = 0
tot2 = 0
for i in range(len(point)):
    tot1 += point[i]
    if tot1 >= 100:
        tot2 = tot1-point[i]
        break
if abs(100-tot1) == abs(100-tot2):
    if tot1 > tot2 :
        print(tot1)
    else:
        print(tot2)
else:
    if abs(100-tot1) > abs(100-tot2):
        print(tot2)
    else:
        print(tot1)
