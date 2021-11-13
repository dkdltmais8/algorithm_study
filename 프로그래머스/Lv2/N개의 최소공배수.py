def solution(arr):
    def lcm(a,b):
        return a*b//gcd(a,b)
    def gcd(a,b):
        while (b):
            a,b = b,a%b
        return a
    while len(arr)>=2:
        a = arr.pop()
        b = arr.pop()
        arr.append(lcm(b,a))
    answer = 0
    answer = arr[0]
    # print(answer)
    return answer
solution([2,6,8,14])
solution([1,2,3])