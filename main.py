#import tweepy module
import tweepy

#setting values for API access
consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""

#setting up Tweepy to search and use twitter API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
#calling API
api = tweepy.API(auth, wait_on_rate_limit = True)#ensures I don't go over rate limit with requests
#search by name method
def searchByName(term, x):
    searchTerm = term
    userList = api.search_users(searchTerm, page=x)
    return userList

#blocking method
def timelineCleanser(searchTerm, pageNum):
    blocked = api.get_blocks()
    while(pageNum <=15):#blocks the first 300 users
        blockables = searchByName(searchTerm, pageNum)
        for user in blockables:
            if(user in blocked):
                print("User " + user.screen_name + " is already blocked.")
            else:
                api.create_block(screen_name=user.screen_name)
                print("User " + user.screen_name + " has been successfully blocked.")
        pageNum = pageNum + 1

if __name__ == '__main__':
    timelineCleanser("term", 1)#substitute "term" for whatever term you want to block

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
