class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        mails={}
        res=[]
        for i in range(len(accounts)):
            for j in range(1,len(accounts[i])):
                if accounts[i][j] not in mails:
                    mails[accounts[i][j]]=[]
                mails[accounts[i][j]].append(i)
        users={}
        for mail in mails:
            for i in range(len(mails[mail])):
                for j in range(i+1,len(mails[mail])):
                    a,b=mails[mail][i],mails[mail][j]
                    users.setdefault(a,[]).append(b)
                    users.setdefault(b,[]).append(a)
        visited=set()
        def dfs(node, group):
            visited.add(node)
            group.append(node)
            for neighbor in users.get(node, []):
                if neighbor not in visited:
                    dfs(neighbor, group)
        groups=[]
        for i in range(len(accounts)):
            if i not in visited:
                group=[]
                dfs(i, group)
                groups.append(group)
        for user in groups:
            res.append([accounts[user[0]][0]])
            acc=[]
            for i in range(len(user)):
                for j in range(1,len(accounts[user[i]])):
                    acc.append(accounts[user[i]][j])
            acc.sort()
            res[-1]+=list(set(acc))
        return res
        
        
                    
                

            