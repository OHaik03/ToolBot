import tweepy
import schedule
import random
import linecache
#from IDS import *

Consumer_Key = '341KcUxlUT3yOuNHX6AV6aeUM'
ConsumerKey_Secret = 'Qted2laW3FqgHKhfg02ZvfGuy5cVhPa1UIfRFIeXeNlv1XdEYQ'
Client = 'd29WNzE4WWpESkhzb0pxSTdxdkE6MTpjaQ'
Client_Secret = 'n6A-8ykKJpL9ySXweSwa128xYx9MXGl-7OBoaKAnlPeqGIZ_jj'
Access_Token = '1822076500742696963-cuNmM72NYVzF3kzXLLmT2D9JQhJJJH'
AccessT_Secret = 'zgwhEM0NvOACKjHz7SE4zWgoK3TALzRBBu8D3cueJ6gY1'


#API Credentials for authenticating the bot
def create_api():

    client = tweepy.Client(
        consumer_key = Consumer_Key,
        consumer_secret = ConsumerKey_Secret,
        access_token = Access_Token,
        access_token_secret = AccessT_Secret
        )
    
    return client  # Return the client object, not Client string

def getMessage():
    
    while True:
        try:    #
            randomInt = random.randint(0, 492)  
            message = linecache.getline("/Users/haik/Desktop/Python Projects/LyricsTool.txt", randomInt)
    
            if not message:
                message = "testing"    
            print(message)
            return message
    
        except FileNotFoundError:
            print("File not found")
            return "bruh"
            break


#function for tweeting
def updateStatus(client: tweepy.Client, message: str):   
    try:     
        client.create_tweet(text = message)
        print('Tweeted!')
        
    except tweepy.TweepyException as e:
        print(f'Error: {e}')
        
def autoTweet():
        updateStatus(authentication, getMessage())

#main function, timer is here
if __name__ == '__main__':
    authentication = create_api()
    randomInt = random.randint(0, 492)  
    print(randomInt)


    schedule.every(10).seconds.do(autoTweet)
    
    try:
        while True:
                schedule.run_pending()

    except KeyboardInterrupt:
        print('Tweeting Stopped')
        
