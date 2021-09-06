import sys
stack = []
N = int(sys.stdin.readline())
for i in range(N):
    a = sys.stdin.readline().rstrip()
    if a == 'top':
        if len(stack) == 0:
            print(-1)
        else:   
            print(stack[-1])
    elif a == 'empty':
        if stack == []:
            print(1)
        else:
            print(0)
    elif a == 'size':
        print(len(stack))
    elif a == 'pop':
        if stack != []:
            print(stack[-1])
            stack.pop(-1)
        else:
            print(-1)
    elif a.split()[0] == 'push':
        stack.append(int(a.split()[-1]))

