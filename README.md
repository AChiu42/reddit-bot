# reddit-bot
 
This is just a reddit bot that supports Bernie Sanders.

## Favorite Thread


## Bot-Counter File Output


## Score
I believe that I deserve a /30 on this assignment. Here is the points breakdown.

1. Each task in `bot.py` is worth 3 points.
   (6 tasks * 3 points/task = 18 points) <b>+18</b>

1. The github repo is worth 2 points. <b>+2</b>

1. Getting at least 100 valid comments posted. <b>+2</b>

1. Getting at least 500 valid comments posted. <b>+2</b>

1. Getting at least 1000 valid comments posted.

1. Make your bot create new submission posts instead of just new comments.
   You can easily automate this process by scanning the top posts in your favorite sub (e.g. /r/liberal or /r/conservative) and posting them to the class sub.
   I recommend creating a separate python file for creating submissions and creating comments.

   For full credit, you must have at least 200 submissions, some of which should be self posts and some link posts.
   Duplicate submissions (i.e. submissions with the same title/selftext/url) do not count. <b>+2</b>

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
   if the comment/submission has a negative sentiment, then downvote it. <b>+4</b>