from textblob import TextBlob
from googletrans import Translator
import tweepy
import time


# Connect Twitter API
def twitter_api():
    mykeys = open('.env', 'r').read().splitlines()

    api_key = mykeys[0]
    api_key_secret = mykeys[1]
    access_token = mykeys[2]
    access_token_secret = mykeys[3]

    auth_handler = tweepy.OAuthHandler(consumer_key=api_key, consumer_secret=api_key_secret)
    auth_handler.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth_handler)

    return api


user_id = []
def printTweetBySearch(s):
    api = twitter_api()
    tweets = tweepy.Cursor(api.search, q = s, include_entities = True, tweet_mode = 'extended', lang = 'ja').items(10)

    for tweet in tweets:
        if tweet.user.screen_name not in user_id:
            print('＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝')
            print('user : ',tweet.user.screen_name)
            user_id.append(tweet.user.screen_name)



def searchTweetsForUser():
    api = twitter_api()

    for user in user_id:
        results = api.user_timeline(screen_name=user, count=5)
        for result in results:
            print('＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝')
            print(result.text)
            print(result.user.screen_name)

def main():
    start = time.time()

    printTweetBySearch("高校生と繋がりたい -filter:retweets")
    searchTweetsForUser()

    end = time.time()
    print(end-start)


# google trans
#translator = Translator(service_urls=['translate.googleapis.com'])
#translation = translator.translate('いい天気ですね！',src='ja', dest='en')
#print(translation.text)


# textblob
#data = TextBlob(translation.text)
#polarity = data.sentiment.polarity

#print("polarity: " + str(polarity))



if __name__=='__main__':
    main()