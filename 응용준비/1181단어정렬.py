
n = int(input())
word = []
new_word = []
for _ in range(n):
    word.append(input())
word = list(set(word))
n = len(word)
for i in range(n):
    new_word.append((len(word[i]), word[i]))
new_word.sort()
for i in range(n):
    print(new_word[i][1])