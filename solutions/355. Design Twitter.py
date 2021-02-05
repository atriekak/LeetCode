class Twitter:
    #Approach: Max-heap with Linked List
    #Time Complexity: O(f) for getNewsFeed; O(1) for rest   // f * 10
    #Space Complexity: O(follower-followee connections + tweets)
    #where, f is the number of users followed by the user queried on
    
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.followed = {}
        self.tweets = {}
        self.time = 0
​
    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        Compose a new tweet.
        """
        if userId not in self.tweets:
            self.follow(userId, userId)     #following oneself if a tweet is posted
            self.tweets[userId] = None
        self.time += 1
        new = ListNode(Tweet(tweetId, self.time))
        new.next = self.tweets[userId]
        self.tweets[userId] = new   
​
    def getNewsFeed(self, userId: int) -> List[int]:
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        """
        ListNode.__lt__ = (lambda a, b : b.tweet.createdAt < a.tweet.createdAt)
        
        heap = []
        fids = self.followed.get(userId, None)
        if fids:
            curr_ftweets = {}
            for fid in fids:
                ftweets = self.tweets.get(fid, None)
                if ftweets:
                    heappush(heap, ftweets)
                    
        result = []
        while len(result) < 10:
            if heap:
                ftweet = heappop(heap)
                result.append(ftweet.tweet.id)
                if ftweet.next:
                    heappush(heap, ftweet.next)
            else:
                break
                            
        return result
​
    def follow(self, followerId: int, followeeId: int) -> None:
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        """
        if followerId not in self.followed:
            self.followed[followerId] = set()
        self.followed[followerId].add(followeeId)
​
    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
