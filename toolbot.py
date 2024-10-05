import tweepy
import schedule
import linecache
import IDS
import saveCount
#can you shuffle all of the lines so that they are all in different places

#API Credentials for authenticating the bot
def create_api():

    client = tweepy.Client(
        consumer_key = IDS.Consumer_Key,
        consumer_secret = IDS.ConsumerKey_Secret,
        access_token = IDS.Access_Token,
        access_token_secret = IDS.AccessT_Secret
        )
    
    return client  # Return the client object, not Client string

def update(newNum):
    from saveCount import setSave
    saveCount.setSave(newNum)
    

def getMessage():#gets the lyrics from the file and returns it to the autoTweet() function
    saveCount.saveCounter += 1
    counter = saveCount.saveCounter
    update(counter)
    
    
    print(saveCount.saveCounter)
    while True:        
        try:    
            
            #sample = open("/Users/haik/Desktop/Python Projects/ShuffledLyricsTool.txt", "r")

            message = linecache.getline("/Users/haik/Desktop/Python Projects/ShuffledLyricsTool.txt", counter)
            #next(sample)
            
            if not message:
                message = "No more lyrics" 
                #sample.close()
                   
            print(message) #prints the tweet
            return message#returns the tweet back to autoTweet()
    
        except FileNotFoundError:
            print("File not found")
            return "bruh"


#function for tweeting
def updateStatus(client: tweepy.Client, message: str):   
    try:     
        client.create_tweet(text = message)
        print('Tweeted!')
        return #Returns back to autoTweet
        
    except tweepy.TweepyException as e:
        print(f'Error: {e}')
        return
        
def autoTweet():#authenticates and gets the message, sends it to the updateStatus function.
        updateStatus(authentication, getMessage())
        return #Returns back to callTime()
        
def callTime():
    schedule.every(10).seconds.do(autoTweet)
    
    
#main function, timer is here
if __name__ == '__main__':
    authentication = create_api()    
    callTime()   
    setter = 0 
    update(setter)#sets the 'saveCounter' variable to 0 
    
    try:
        while True:
                schedule.run_pending()

    except KeyboardInterrupt:
        print('Tweeting Stopped')
        
