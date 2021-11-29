# reddit-bot
 
This is just a reddit bot that supports Bernie Sanders. Here is the link to the [project description](https://github.com/mikeizbicki/cmc-csci040/blob/2021fall/hw_04/README.md) if that's what you're into.

## Favorite Thread

<img width=500, alt = 'thread screenshot', src='https://github.com/AChiu42/reddit-bot/blob/main/Bernie-Comment-Thread.png'>
[link to favorite thread](https://old.reddit.com/r/BotTown2/comments/r4fyuz/she_said_yelling_at_a_worker_over_masks_was/hmgo9nd/)

I enjoyed this comment thread because of how many bots here were supporting Bernie. They all are working to support **The Cause**, which is getting Bernie Sanders in his rightful position as President.

## Bot-Counter File Output
```
len(comments)= 1000
len(top_level_comments)= 473
len(replies)= 527
len(valid_top_level_comments)= 473
len(not_self_replies)= 527
len(valid_replies)= 527
========================================
valid_comments= 1000
========================================
```
*This was the output of running the bot.py file a little while back. I ran it a few more times to try and get some other extra credit and it may have changed/lowered the output. No I don't have a screenshot. I forgot because I'm dumb...>_<'*

## Score
I believe that I deserve a 32/30 on this assignment. Here is the points breakdown:

1. Each task in `bot.py` is worth 3 points.
   (6 tasks * 3 points/task = 18 points) **+18**

1. The github repo is worth 2 points. **+2**

1. Getting at least 100 valid comments posted. **+2**

1. Getting at least 500 valid comments posted. **+2**

1. Getting at least 1000 valid comments posted.**+2**

1. Make your bot create new submission posts instead of just new comments.
   You can easily automate this process by scanning the top posts in your favorite sub (e.g. /r/liberal or /r/conservative) and posting them to the class sub.
   I recommend creating a separate python file for creating submissions and creating comments.

   For full credit, you must have at least 200 submissions, some of which should be self posts and some link posts.
   Duplicate submissions (i.e. submissions with the same title/selftext/url) do not count. **+2**

1. Create an "army" of 5 bots that are all posting similar comments.
   This will require creating 5 different reddit accounts.
   You can use the same code for each bot (but different `praw.ini` files with the corresponding login credentials).
   The challenge is keeping all 5 of these bots running simultaneously.
   Each bot needs to post at least 500 valid comments to get this extra credit.

1. Instead of having your bot reply randomly to posts,
   make your bot reply to the most highly upvoted comment in a thread that it hasn't already replied to.
   Since reddit sorts comments by the number of upvotes, this will ensure that your bot's comments are more visible.
   You will still have to ensure that your bot never replies to itself if your bot happens to have the most upvoted comment.

1. Have your bot upvote any comment or submission that mentions your favorite candidate (or downvote submission mentioning a candidate you do not like).
   I recommend creating a separate python file for performing the upvotes,
   and you must be able to upvote comments contained within any submission in the class subreddit.

   You may earn an additional two points if you use the [TextBlob](https://textblob.readthedocs.io/en/dev/) sentiment analysis library to determine the sentiment of all the posts that mention your favorite candidate.
   If the comment/submission has positive sentiment, then upvote it;
   if the comment/submission has a negative sentiment, then downvote it. **+4**

As stated above, I completed the tasks: 6 tasks in the bot.py file **+18**, github repo **+2**, at least 100, 500, and 1000 comments **+6**, make a bot post at least 200 submissions **+2**, and upvote/downvote any comment or submission that mentions Bernie Sanders or his political opponents using the TextBlob sentiment analysis library **+4**, bringing the total up to **32/30**.