s = input()
stack = []
comparison = ["P","P","A","P"]
if s == "P" or s == "PPAP":
    print("PPAP")
else:
    for i in s:
        stack.append(i)
        if stack[-4:] == comparison:
            for _ in range(3):
                stack.pop()
    if stack == comparison or stack ==['P']:
        print("PPAP")
    else:
        print("NP")
