class unionFind:
    def __init__(self,n):
        self.parent=list(range(n))
    def find(self,x):
        if self.parent[x]==x:
            return x
        else:
            self.parent[x]=self.find(self.parent[x])
            return self.parent[x]
    def union(self,a,b):
        pa=self.find(a)
        pb=self.find(b)
        self.parent[pb]=pa

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        users=unionFind(len(accounts))
        mails={}
        res=[]
        for i in range(len(accounts)):
            for j in range(1,len(accounts[i])):
                email=accounts[i][j]
                if email not in mails:
                    mails[email]=i
                else:
                    users.union(i,mails[email])
        
        group={}
        for i in range(len(accounts)):
            root=users.find(i)
            group.setdefault(root,[]).append(i)
        for root,user in group.items():
            res.append([accounts[root][0]])
            acc=[]
            for i in user:
                for j in range(1,len(accounts[i])):
                    acc.append(accounts[i][j])
            acc=sorted(set(acc))
            res[-1]+=acc
        
        return res
