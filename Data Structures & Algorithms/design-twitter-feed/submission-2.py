class Twitter:

    def __init__(self):
        self.time=0
        self.ut={}
        self.uu={}

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time+=1
        if userId not in self.ut:
            self.ut[userId]=[]
        self.ut[userId].append((-self.time,tweetId))


    def getNewsFeed(self, userId: int) -> List[int]:
        h=[]
        res=[]
        user=[]
        if userId in self.uu:
            user=self.uu[userId] 
        users=[userId]
        for x in user:
            users.append(x) 
        users=set(users)      
        for x in users:
            if x in self.ut:
                for y in self.ut[x]:
                    h.append(y)
        heapq.heapify(h)
        for _ in range(min(10,len(h))):
            x,y=heapq.heappop(h)
            res.append(y)
        return res
        
        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.uu:
            self.uu[followerId]=set()
            #self.uu[followerId].add(followerId)
        self.uu[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.uu:
            self.uu[followerId].discard(followeeId)



