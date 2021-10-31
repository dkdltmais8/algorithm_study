def calc(a, b, op):
    a,b = int(a),int(b)
    if op == '*':
        return a * b
    elif op == '+':
        return a + b
    elif op == '-':
        return a - b
def solution(expression):
    answer = 0
    orders = [[0,1,2],[0,2,1],[1,0,2],[1,2,0],[2,1,0],[2,0,1]]
    operand = ['*','+','-']
    num = expression
    for i in operand:
        num = num.replace(i,' ')
    num = num.split(' ')
    print(num)
    now_op = [op for op in expression if not op.isdigit()]
    print(now_op)
    for order in orders:
        n = num
        op = now_op
        for i in range(3):
            stack_num = []
            stack_op = []
            stack_num.append(n[0])
            for j in range(len(op)):
                stack_num.append(n[j+1])
                stack_op.append(op[j])
                if stack_op[-1] == operand[order[i]]:
                    a = stack_num.pop()
                    b = stack_num.pop()
                    cal = stack_op.pop()
                    stack_num.append(calc(a,b,cal))
            n = stack_num
            op = stack_op
        answer = max(answer,abs(n[0]))
        print(answer)
    return answer
solution("100-200*300-500+20")