import praw
import datetime
import time
import prawcore
from textblob import TextBlob

reddit = praw.Reddit('bot1')

post_upvotes = 0
post_downvotes = 0
comment_upvotes = 0
comment_downvotes = 0

for submission in list(reddit.subreddit("BotTown2").hot(limit=150)):
    submission.comments.replace_more(limit=10, threshold=0)
    blob = TextBlob(str(submission.title))
    sentiment = blob.sentiment.polarity
    not_my_comments = []
    print('processing submission')

    if 'Bernie' in submission.title or 'Sanders' in submission.title or 'Bernie Sanders' in submission.title:
        if str(submission.author) != 'SomeBottomText':
            if sentiment > 0:
                submission.upvote()
                post_upvotes += 1
                # print('good post')
            if sentiment <= 0:
                submission.downvote()
                post_downvotes += 1
                # print('bad post')
    if 'Trump' in submission.title or 'Biden' in submission.title or 'Putin' in submission.title or 'GOP in submission.title':
        if str(submission.author) != 'SomeBottomText':
            if sentiment <= 0:
                submission.upvote()
                post_upvotes += 1
                # print('good post')
            if sentiment > 0:
                submission.downvote()
                post_downvotes += 1
                # print('bad post')
    for comment in submission.comments:
        if str(comment.author) != 'SomeBottomText':
            not_my_comments.append(comment)
    for comment in not_my_comments:
        blob = TextBlob(str(comment.body))
        sentiments = blob.sentiment.polarity
        try:
            if 'Bernie' in comment.body or 'Sanders' in comment.body or 'Bernie Sanders' in comment.body:
                if sentiments > 0:
                    comment.upvote()
                    comment_upvotes += 1
                    # print('good comment')
                if sentiments <= 0:
                    comment.downvote()
                    comment_downvotes += 1
                    # print('bad comment')
            if 'Trump' in comment.body or 'Biden' in comment.body or 'Putin' in comment.body or 'GOP in submission.title':
                if sentiments <= 0:
                    comment.upvote()
                    comment_upvotes += 1
                    # print('good comment')
                if sentiments > 0:
                    comment.downvote()
                    comment_downvotes += 1
                    # print('bad comment')
        except prawcore.exceptions.NotFound:
            print('Deleted Comment')
            pass
        for reply in comment.replies:
            try:
                if 'Bernie' in reply.body or 'Sanders' in reply.body or 'Bernie Sanders' in reply.body:
                    if sentiments > 0:
                        reply.upvote()
                        comment_upvotes += 1
                        # print('good comment')
                    if sentiments <= 0:
                        reply.downvote()
                        comment_downvotes += 1
                        # print('bad comment')
                if 'Trump' in reply.body or 'Biden' in reply.body or 'Putin' in reply.body or 'GOP in submission.title':
                    if sentiments <= 0:
                        reply.upvote()
                        comment_upvotes += 1
                        # print('good comment')
                    if sentiments > 0:
                        reply.downvote()
                        comment_downvotes += 1
                        # print('bad comment')
            except prawcore.exceptions.NotFound:
                print('Deleted Comment')
                pass
        

    total_post_votes = post_upvotes + post_downvotes
    total_comment_votes = comment_upvotes + comment_downvotes

    print('number of upvotes=', post_upvotes + comment_upvotes)
    print('number of downvotes=', post_downvotes + comment_downvotes)
    print('current number of post up/downvotes=', total_post_votes)
    print('current number of comment up/downvotes=', total_comment_votes)

print('number of post upvotes=', post_upvotes)
print('number of post downvotes=', post_downvotes)
print('number of comment upvotes=', comment_upvotes)
print('number of comment downvotes=', comment_downvotes)
print('number of post up/downvotes=', total_post_votes)
print('number of comment up/downvotes=', total_comment_votes)