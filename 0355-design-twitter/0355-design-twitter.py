from typing import List

class Twitter:

    def __init__(self):
        self.count = 0
        self.following = defaultdict(set)
        self.tweets = defaultdict(list) 

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append([self.count, tweetId])
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        # Include the user's own tweets in their feed
        minHeap = []
        res = []

        self.following[userId].add(userId)
        for followee in self.following[userId]:
            if followee in self.tweets:
                index = len(self.tweets[followee]) - 1
                count, tweetId = self.tweets[followee][index]
                minHeap.append([count, tweetId, followee, index - 1])
        heapq.heapify(minHeap)
        while minHeap and len(res) < 10:
            count, tweetId, followee, index = heapq.heappop(minHeap)
            res.append(tweetId)

            if index >= 0:
                count, tweetId = self.tweets[followee][index]
                heapq.heappush(minHeap, [count, tweetId, followee, index - 1])
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)
