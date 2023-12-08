import tweepy 
from time import sleep 
# from credentials import consumer_key, consumer_secret, access_token, access_token_secret
from config import QUERY, FOLLOW, LIKE, SLEEP_TIME 

# auth = tweepy.OAuthHandler(consumer_key, consumer_secret) 
# auth.set_access_token(access_token, access_token_secret) 
# client = tweepy.Client(
# 	consumer_key=consumer_key, 
# 	consumer_secret=consumer_secret,
# 	access_token=access_token,
# 	access_token_secret=access_token_secret
# 	)
auth = tweepy.OAuth1UserHandler(
    'zPuHCFIpLtXnHn34SxrwFRw8V', #API key
	'lEIQ8VHryfZyRuNTUH94uW4SwD9BRxjyLcNhrhlK9U4UGjPnMr', #API Key Secret
	'1729021708554899456-A9ExsNVMQkrrTLwyVskjqEa9b8Z8et', #Access Token
	'fPBPWEm9t5abPcZKbUnZbvka624Az10gerpeYwSGnC4LT' #Access Token Secret
)

api = tweepy.API(auth) 

tweet = api.update_status("Hello world!")
# print("Twitter bot which retweets, like tweets and follow users") 
# print("Bot Settings") 
# print("Like Tweets :", LIKE) 
# print("Follow users :", FOLLOW) 

# for tweet in tweepy.Cursor(api.search_tweets, q=QUERY).items():

# 	try: 
# 		print('\nTweet by: @' + tweet.user.screen_name) 

# 		tweet.retweet() 
# 		print('Retweeted the tweet') 

# 		# Favorite the tweet 
# 		if LIKE: 
# 			tweet.favorite() 
# 			print('Favorited the tweet') 

# 		# Follow the user who tweeted 
# 		# check that bot is not already following the user 
# 		if FOLLOW: 
# 			if not tweet.user.following: 
# 				tweet.user.follow() 
# 				print('Followed the user') 

# 		sleep(SLEEP_TIME) 

# 	except tweepy.TweepError as e: 
# 		print(e.reason) 

# 	except StopIteration: 
# 		break
