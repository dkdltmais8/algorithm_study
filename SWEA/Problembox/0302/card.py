def rsp(l_idx,r_idx):
	l,r = board[l_idx-1], board[r_idx-1]
	if l == r:
		return l_idx
	elif l == 1:
		if r == 2:
			return r_idx
		elif r == 3:
			return l_idx
	elif l == 2:
		if r == 1:
			return l_idx
		elif r == 3:
			return r_idx
	elif l == 3:
		if r == 1:
			return r_idx
		elif r == 2:
			return l_idx

def slice(start, end):
	if start == end:
		return start
	else:
		mid = (start+end) // 2
		start = slice(start,mid)
		end = slice(mid+1,end)
		return rsp(start,end)
for tc in range(1, int(input())+1):
	n = int(input())
	board = list(map(int,input().split()))
	print("#{} {}".format(tc, slice(1,n)))