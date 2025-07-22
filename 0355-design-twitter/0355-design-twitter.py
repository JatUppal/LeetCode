from typing import List

class Twitter:

    def __init__(self):
        self.following = {}  # {followerId: set of followeeIds}
        self.tweets = []     # list of [userId, tweetId]

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets.append([userId, tweetId])

    def getNewsFeed(self, userId: int) -> List[int]:
        # Include the user's own tweets in their feed
        feed_users = self.following.get(userId, set()) | {userId}
        res = []

        # Traverse tweets from most recent to oldest
        for i in range(len(self.tweets) - 1, -1, -1):
            if self.tweets[i][0] in feed_users:
                res.append(self.tweets[i][1])
            if len(res) == 10:
                break

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.following:
            self.following[followerId] = set()
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.following:
            self.following[followerId].discard(followeeId)
