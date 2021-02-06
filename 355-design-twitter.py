from collections import defaultdict, deque
from itertools import islice
from heapq import merge
from time import time


class Twitter:
    def __init__(self):
        self.news_feed_size = 10
        self.tweets = defaultdict(deque)
        self.followees = defaultdict(set)

    def postTweet(self, user: int, tweet: int) -> None:
        self.tweets[user].appendleft((-time(), tweet))

    def getNewsFeed(self, user: int) -> list[int]:
        tweets = merge(*[self.tweets[followee] for followee in self.followees[user] | {user}])
        return [tweet for _, tweet in islice(tweets, self.news_feed_size)]

    def follow(self, follower: int, followee: int) -> None:
        self.followees[follower].add(followee)

    def unfollow(self, follower: int, followee: int) -> None:
        self.followees[follower].discard(followee)
