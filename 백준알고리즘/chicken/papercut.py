n, m = map(int,input().split())
n_list = [0,n]
m_list = [0,m]
for i in range(int(input())):
    dir,length = map(int,input().split())
    if dir == 0:
        m_list.append(length)
    else:
        n_list.append(length)
n_list.sort()
m_list.sort()
result = 0
for i in range(1,len(n_list)):
    for j in range(1,len(m_list)):
        width = n_list[i] - n_list[i-1]
        height = m_list[j] - m_list[j-1]
        result = max(result,width * height)
print(result)