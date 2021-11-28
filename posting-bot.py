import praw
import random
import time

reddit = praw.Reddit('bot1')
post = list(reddit.subreddit('NeutralPolitics').hot(limit = 100)) #dankmemes
for i in range(225):
    try:
        sub = random.choice(post)
        title = sub.title
        text = sub.selftext
        url = sub.url
        reddit.validate_on_submit = True
        print('len(url)=', len(url))
        print('len(text)=', len(text))
        if i == 69:
            print('nice')     
        if len(text) > 9 * len(url): # post text posts if text is longer than 9 * len(url) 
            reddit.subreddit('BotTown2').submit(title, selftext= text)
            print("text post # ", i)
        else: # post url post if not
            reddit.subreddit('BotTown2').submit(title, url= url)
            print("url post # ", i)
    except praw.exceptions.InvalidURL:
        print('url not valid')
        pass
    time.sleep(46) # keep short for testing, set back to 46 when running
    