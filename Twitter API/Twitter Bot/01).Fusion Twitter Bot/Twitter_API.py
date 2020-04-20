# importing modules that are required
import tweepy

#Storing credentials within variables
consumer_key = 'JUwlrJDma6bE274e3nmBchJQc'
consumer_secret = 'W5bziwhdWZjUEiHMzY16dNanxsdpuLxcJ7vhizslHgTaiqBf9S'
access_token = '1251774870121263104-GppJz4zIc4Z9kKYlLGAmLGNGJV25VV'
access_token_secret = '5xJiQ2oUKzRI2L8a86e0HfwlP7SMQaLFk9iTc377WXuBI'

#To authenticate the account with tweepy.
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
user = api.me()

#simply loop through followers and then follow each one.
for follower in tweepy.Cursor(api.followers).items():
    print(type(follower))
    follower.follow()
    print ("Followed everyone that is following " + user.name)

#To get the details of your followers
#To print your screen_name
print(user.screen_name)

#To count your followers
print ("Number of followers are :- {}".format(user.followers_count))

#To get detail about your about our friends
for friend in user.friends():
    print("Friend name is :- {}".format(friend.name))
    print("Friend location is :- {}".format(friend.location))
    print ("Friend screen name is :- {}".format(friend.screen_name))
    print("Friend description is :- {}".format(friend.description))

#Retweet a Tweet based on keywords.
#Enter the keyword
search = input("Keyword")

#Number of tweet you wish to interact
numberOfTweets = int(input("Number of tweets you wish to interact with"))

for tweet in tweepy.Cursor(api.search, search).items(numberOfTweets):
    try:
        tweet.retweet()
        print('Retweeted the tweet')
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break

#Reply to the user based on the keyboard
#Enter the keyword
search = input("Keyword")

#Number of tweet you wish to interact
numberOfTweets = int(input("Number of tweets you wish to interact with"))

#Enter the phase that you want to reply.
phrase = input("What you would like your response tweet to say")
for tweet in tweepy.Cursor(api.search, search).items(numberOfTweets):
    try:
        tweetId = tweet.user.id
        username = tweet.user.screen_name
        api.update_status("@" + username + " " + phrase, in_reply_to_status_id = tweetId)
        print ("Replied with " + phrase)

    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break
