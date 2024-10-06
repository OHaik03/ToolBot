import tweepy
import schedule
import linecache
import saveCount


#API Credentials for authenticating the bot
def create_api():
    import IDS

    client = tweepy.Client(
        consumer_key = IDS.Consumer_Key,
        consumer_secret = IDS.ConsumerKey_Secret,
        access_token = IDS.Access_Token,
        access_token_secret = IDS.AccessT_Secret
        )
    
    return client  # Return the client object

def update(newNum): #meant to save the position in the list of lyrics
    from saveCount import setSave
    saveCount.setSave(newNum)
    return
    

def getMessage():#gets the lyrics from the file and returns it to the autoTweet() function
    saveCount.saveCounter += 1
    counter = saveCount.saveCounter
    update(counter)
    
    
    print(saveCount.saveCounter)
    while True:        
        try:    
            message = linecache.getline("/Users/haik/Desktop/Python Projects/ShuffledLyricsTool.txt", counter)
            
            if not message:
                message = "No more lyrics" 
                   
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
    schedule.every(6).hours.do(autoTweet)
    
    
#main function
if __name__ == '__main__':
    authentication = create_api()    
    callTime()   
    
    try:
        while True:
                schedule.run_pending()

    except KeyboardInterrupt:
        print('Tweeting Stopped')
        
