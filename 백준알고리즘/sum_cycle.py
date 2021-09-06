N = int(input())
N1 = N
result = -1
cnt = 0

while N != result:
    if 99 >= N1 >= 10:
        result = (N1 % 10) + (N1 // 10)
        result = (result % 10) + ((N1 % 10)*10) 
        cnt += 1
        N1 = result
      
    elif 0 <= N1 < 10:
        result = (N1 % 10) + (N1 // 10)
        result = (result % 10) + ((N1 % 10)*10) 
        cnt += 1
        N1 = result
       
      

    else:
        print('안돼. 돌아가')
        break

print(cnt)
    
    