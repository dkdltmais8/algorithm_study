def solution(numbers):
    answer = []
    for i in numbers:
        if not i%2:
            answer.append(i+1)
        else:
            a = ['0']+list(bin(i)[2:])
            idx = ''.join(a).rfind('0')
            a[idx],a[idx+1] = '1','0'
            b = int(''.join(a),2)
            answer.append(b)
    return answer
solution([2,7])