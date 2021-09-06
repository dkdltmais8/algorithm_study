
for i in range(10):
    length = int(input())
    num = list(map(int,input().split()))
    N = int(input())
    func = list(input().split())
    for j in range(len(func)):
        if func[j] == "I":
            for k in range(int(func[j+2])):
                num.insert(int(func[j+1])+k,int(func[j+k+3]))
        if func[j] == "D":
            for k in range(int(func[j+2])):
                del num[int(func[j+1])]
        if func[j] == "A":
            for k in range(int(func[j+1])):
                num.append(int(func[j+k+2]))
    print(f"#{i+1}" , end=' ')
    for j in range(10):
        print(f"{num[j]}", end = ' ')
    print()


