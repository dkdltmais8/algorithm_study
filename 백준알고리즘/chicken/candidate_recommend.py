n = int(input())
vote = int(input())
student = list(map(int, input().split()))
picture = {}
for i in range(vote):
    if picture.get(student[i]):
        picture[student[i]] += 1
    else:
        if len(picture) == n:
            min_vote = vote
            for j in picture:
                if picture[j] < min_vote :
                    min_vote = picture[j]
                    min_idx = j
                elif picture[j] == min_vote:
                    for k in range(i):
                        if student[k] == min_idx:
                            break
                        if student[k] == j:
                            min_vote = student[j]
                            min_idx = j
                            break
            for _ in range(min_vote):
                student[student.index(min_idx)] = -1

            del picture[min_idx]
        picture[student[i]] = 1


ans = sorted(picture)
print(*ans)


n = int(input())
vote = int(input())
student = list(map(int, input().split()))
picture = {}
for i in range(vote):
    if picture.get(student[i]):
        picture[student[i]] += 1
    else:
        if len(picture) == n:
            min_vote = vote
            for j in picture:
                if picture[j] < min_vote :
                    min_vote = picture[j]
                    min_idx = j
            del picture[min_idx]
        picture[student[i]] = 1
    for j in picture:
        picture[j] -= 0.000000001
ans = sorted(picture)
print(*ans)