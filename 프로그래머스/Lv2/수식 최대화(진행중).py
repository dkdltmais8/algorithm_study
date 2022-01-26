from itertools import permutations
def calc(a, b, op):
    a,b = int(a),int(b)
    if op == '*':
        return str(a * b)
    elif op == '+':
        return str(a + b)
    elif op == '-':
        return str(a - b)
def cal(lst,op):
    arr = []
    temp = ''
    for i in lst:
        if i.isdigit():
            temp += i
        else:
            arr.append(temp)
            arr.append(i)
            temp = ""
    arr.append(temp)
    for i in op:
        s = []
        while arr:
            now = arr.pop(0)
            if now == i:
                s.append(calc(s.pop(),arr.pop(0),i))
            else:
                s.append(now)
        arr = s
    return abs(int(arr[0]))

def solution(expression):
    operand = ['*','+','-']
    operand = list(permutations(operand,3))
    ans = []
    for i in operand:
        ans.append(cal(expression,i))
    return ans
solution("100-200*300-500+20")