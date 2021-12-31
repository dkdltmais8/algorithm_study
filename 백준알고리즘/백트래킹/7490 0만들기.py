for tc in range(int(input())):
    arr = [i for i in range(1,int(input())+1)]
    def dfs(depth,sentence):
        global ans
        if depth == len(arr)+1:
            if check(sentence):
                ans.append(sentence)
            return
        dfs(depth+1,sentence+' '+str(depth))
        dfs(depth + 1, sentence + '+' + str(depth))
        dfs(depth + 1, sentence + '-' + str(depth))
    def check(s):
        fake = s.replace(' ','')
        if eval(fake) == 0:
            print(s)
    dfs(2,'1')
    print()