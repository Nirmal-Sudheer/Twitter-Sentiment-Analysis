from textblob  import TextBlob
import tweepy
import sys


api_key='Xxp7vyRcQU5wObGwObUbD98Jf'
api_key_secret='ZKmQZsmHcC9MrRzVx7HLQythiJJUtPkCx4cAW2numCOlEzGI4f'

access_token='1273967088785211395-LD3AjNwMxYQ2Nn5djOa10Jw0dKlwat'
access_token_secret='MGNZVpkUyNtSdMpgOEo4EChYiLk9rrVhaICYglKfeAV9R'

auth_handler=tweepy.OAuthHandler(consumer_key=api_key, consumer_secret=api_key_secret)
auth_handler.set_access_token(access_token,access_token_secret)

api=tweepy.API(auth_handler)

search_term='stonks'
tweet_amount=200

tweets=tweepy.Cursor(api.search_tweets,q=search_term,lang='en').items(tweet_amount)

polarity = 0   #10 means +ve text,-10 means highly -ve
positive=0
negative=0
neutral=0



for tweet in tweets:
    final_text=tweet.text.replace('RT','')

    if final_text.startswith(' @'):
        postion=final_text.index(':')
        final_text=final_text[postion+2:]
    
    if final_text.startswith('@'):
        postion=final_text.index(' ')
        final_text=final_text[postion+2:]


    analysis=TextBlob(final_text)
    tweet_polarity=analysis.polarity
    
    
    if tweet_polarity > 0.00:
        positive +=1
    
    elif tweet_polarity <0.00:
        negative +=1

    elif tweet_polarity == 0.00:
        neutral += 1
    polarity +=tweet_polarity

print(polarity)

if polarity >20:
    print(f'The tweet is overall positive with an overall polarity of {polarity}')

elif polarity<20:
        print(f'The tweet is overall negative with a polarity of {polarity}')

elif polarity==20:
        print(f'The tweet is overall neutral with a polarity of {polarity}')


print(f'Amount of  positive tweets: {positive}')
print(f'Amount of  negative tweets: {negative}')
print(f'Amount of  neutral tweets: {neutral}')












