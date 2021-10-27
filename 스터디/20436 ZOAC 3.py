board = {'q':(0,0),'w':(0,1),'e':(0,2),'r':(0,3),'t':(0,4),'y':(0,5),'u':(0,6),'i':(0,7),'o':(0,8),'p':(0,9),
         'a':(1,0),'s':(1,1),'d':(1,2),'f':(1,3),'g':(1,4),'h':(1,5),'j':(1,6),'k':(1,7),'l':(1,8),
         'z':(2,0),'x':(2,1),'c':(2,2),'v':(2,3),'b':(2,4),'n':(2,5),'m':(2,6)}
left,right = map(str,input().split())
lx,ly = board[left]
rx,ry = board[right]
ans = list(input())
tot = 0
left_sol = "qwertasdfgzxcv"
for i in ans:
    px,py = board[i]
    if i in left_sol:
        tot += abs(lx - px) + abs(ly - py) + 1
        lx,ly = px,py
    else:
        tot += abs(rx-px)+abs(ry-py)+1
        rx,ry = px,py
print(tot)

# lst = ['qwertyuiop','asdfghjkl','zxcvbnm']
# dic = dict()
# for i in range(3):
#     for j in range(len(i)):
#         dic[lst[i][j]] = (i,j)