#Import required Modules
import webbrowser
import requests
import tweepy
import json

#Creat a class which contain all the function to handle account
class Twitter_Account:

    def __init__(self,consumer_key,consumer_secret,access_token,access_token_secret):
        self.consumer_key = consumer_key
        self.consumer_secret= consumer_secret
        self.access_token =access_token
        self.access_token_secret = access_token_secret

    #Function to authenticate the account with tweepy.
    def access(self):
        auth = tweepy.OAuthHandler(self.consumer_key,self.consumer_secret)
        auth.set_access_token(self.access_token,self.access_token_secret)
        return tweepy.API(auth) # returns api object

    #Post the quote on my twitter Account.
    def post(self,quote_details):
        self.access().update_status('"%s." \n-%s \n\n Daily Inspiration From Reflection' % (quote_details))


#Get the daily quote after passing url to it.
def get_quote(url):
    response = requests.get(url)
    quote_info = json.loads(response.content).get('contents').get('quotes')[0]
    quote = quote_info.get('quote')
    author = quote_info.get('author')
    return quote,author

#Storing credentials within variables
consumer_key = 'JUwlrJDma6bE274e3nmBchJQc'
consumer_secret = 'W5bziwhdWZjUEiHMzY16dNanxsdpuLxcJ7vhizslHgTaiqBf9S'
access_token = '1251774870121263104-GppJz4zIc4Z9kKYlLGAmLGNGJV25VV'
access_token_secret = '5xJiQ2oUKzRI2L8a86e0HfwlP7SMQaLFk9iTc377WXuBI'
url = 'http://quotes.rest/qod.json?category=inspire'


#Creating the object for Class Twitter_Account
twitter_acc = Twitter_Account(consumer_key,consumer_secret,access_token,access_token_secret)
twitter_acc.access()
twitter_acc.post(get_quote(url))
print("Quote posted")
