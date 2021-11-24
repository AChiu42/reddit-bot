import praw
import random
import datetime
import time

# FIXME:
# copy your generate_comment functions from the madlibs assignment here

reddit = praw.Reddit('bot1')
url = "https://old.reddit.com/r/BotTown/comments/qzbz12/test_text_postjust_ignore_for_somebottomtext/?sort=new"
submission = reddit.submission(url=url)


# Make it a somewhat political statement
# CHANGE IT FROM THE MADLIBS LAB

madlibs_1 = [
    "[AMERICA] [MESSED UP] when we did not put [BERNIE] in the White House." " Did [NOBODY] see the way [HE] sits in a chair?",
    ]

madlibs_2 = [
    "It is a [TRUE] [TRAGEDY] what [AMERICA] has turned into." " Why can't people be more more like [JEFF] or [ELON]?" " [EVERYONE] [LOVES] [BILLIONAIRES]."
    ]

madlibs_3 = [
    "[BILLIONAIRES] have it [ROUGH]." " Imagine paying over a billion dollars [IN TAXES] and it still hardly affects your [WEALTH]." "What a [TRAGEDY]." " If [BERNIE] were [PRESIDENT], they would be paying MUCH MORE in taxes."
    ]

madlibs_4 = [
    "[AMERICA] used to be a [SYMBOL] for the world." " Now it is just run by [CLOWNS] who are [INEPT] and out of touch with [AMERICANS]."
    ]

madlibs_5 = [
    "[AMERICA] [REQUIRES] dramatic change [IMMEDIATELY]." " [AMERICANS] dwell on the past too much when they really should be moving on from the [INEPT] [TRUMP]." " He does not deserve anymore attention than what he already gets."
    ]

madlibs_6 = [
    "How can [AMERICANS] be expected to be [UPSTANDING] [CITIZENS] when our [POLITICIANS] fight over decisions that hardly affect them?" " [EVERYONE] needs to relearn what democracy means and unite as one nation and one people, or else [AMERICA] will not be around for much longer."
]

replacements = {
    'PYTHON' : ['Python', 'Programming', 'Coding'],
    'AMERICA' : ['America', 'This country', 'This great country', 'The United States', 'The United States of America'],
    "BERNIE" : ['Bernie', 'Bernie Sanders', 'Our Lord and Savior Bernie Sanders'],
    'MESSED UP' : ['messed up', 'screwed up', 'made a mistake'],
    'NOBODY' : ['nobody', 'no one'],
    'HE' : ['Bernie', 'Bernie Sanders'],
    'TRAGEDY' : ['tragedy', 'shame'],
    'TRUE' : ['true', 'real'],
    'JEFF' : ['Jeff Bezos', 'Jeff', 'that Amazon CEO guy'],
    'ELON' : ['Elon', 'Elon Musk', 'the musky dude that runs Telsa', 'the elongated muskrat'],
    'EVERYONE' : ['Everyone', 'All people', 'Americans'],
    'LOVE' : ['love', 'like', 'appreciate'],
    'BILLIONAIRES' : ['Billionaires', 'The rich folks', 'The top 1%'],
    'PRESIDENT' : ['President', 'in office', 'The President', 'in the White House'],
    'ROUGH' : ['rough', 'tough'],
    'IN TAXES' : ['in taxes', 'to the government', 'every year'],
    'WEALTH' : ['wealth', 'net worth', 'spare tens of billions'],
    'SYMBOL' : ['Beacon of Hope', 'symbol of peace and power', 'role model'],
    'CLOWNS' : ['clowns', 'fools'],
    'INEPT' : ['inept', 'old', 'useless'],
    'AMERICANS' : ['Americans', 'the American people', 'the people of this country', 'the everyday person'],
    'REQUIRES' : ['requires', 'needs', 'is desperate for'],
    'IMMEDIATELY' : ['immediately', 'at this instant', 'right now', 'as soon as possible'],
    'TRUMP' : ['Trump', 'Former President', 'Donald Trump'],
    'LOVES' : ['adores', 'loves', 'likes'],
    'UPSTANDING' : ['upstanding', 'model', 'good'],
    'CITIZENS' : ['citizens', 'people', 'Americans'],
    'POLITICIANS' : ['politicians', "country's leaders", 'Representatives', 'Congressmen and Congresswomen']
    }

all_sentences = [madlibs_1, madlibs_2, madlibs_3, madlibs_4, madlibs_5, madlibs_6]

submission.comments.replace_more(limit=None) # keep small when testing, change to None when actually running

def generate_comment():
    '''
    This function generates random comments according to the patterns specified in the `madlibs` variable.
    To implement this function, you should:
    1. Randomly select a string from the madlibs list.
    2. For each word contained in square brackets `[]`:
        Replace that word with a randomly selected word from the corresponding entry in the `replacements` dictionary.
    3. Return the resulting string.
    For example, if we randomly seleected the madlib "I [LOVE] [PYTHON]",
    then the function might return "I like Python" or "I adore Programming".
    Notice that the word "Programming" is incorrectly capitalized in the second sentence.
    You do not have to worry about making the output grammatically correct inside this function.
    '''
    r = (random.choice(all_sentences))
    s = random.choice(r)
    for k in replacements:
        s = s.replace('['+k+']', random.choice(replacements[k]))
    return s


# connect to reddit 
# reddit = praw.Reddit('bot1')

# connect to the debate thread, but can change later
# reddit_debate_url = 'https://old.reddit.com/r/BotTown/comments/qzbz12/test_text_postjust_ignore_for_somebottomtext/?'
# submission = reddit.submission(url=reddit_debate_url)


# each iteration of this loop will post a single comment;
# since this loop runs forever, your bot will continue posting comments forever;
# (this is what makes it a deamon);
# recall that you can press CTRL-C in the terminal to stop your bot
#
# HINT:
# while you are writing and debugging your code, 
# you probably don't want it to run in an infinite loop;
# you can change this while loop to an if statement to make the code run only once
if True: # change IF TO WHILE LATER

    # printing the current time will help make the output messages more informative
    # since things on reddit vary with time
    print()
    print('new iteration at:',datetime.datetime.now())
    print('submission.title=',submission.title)
    print('submission.url=',submission.url)

    # FIXME (task 0): get a list of all of the comments in the submission
    # HINT: this requires using the .list() and the .replace_more() functions
    # submission.comments.replace_more(limit=None)
    all_comments = submission.comments.list()
    # HINT: 
    # we need to make sure that our code is working correctly,
    # and you should not move on from one task to the next until you are 100% sure that 
    # the previous task is working;
    # in general, the way to check if a task is working is to print out information 
    # about the results of that task, 
    # and manually inspect that information to ensure it is correct; 
    # in this specific case, you should check the length of the all_comments variable,
    # and manually ensure that the printed length is the same as the length displayed on reddit;
    # if it's not, then there are some comments that you are not correctly identifying,
    # and you need to figure out which comments those are and how to include them.
    print('len(all_comments)=',len(all_comments))

    # FIXME (task 1): filter all_comments to remove comments that were generated by your bot
    # HINT: 
    # use a for loop to loop over each comment in all_comments,
    # and an if statement to check whether the comment is authored by you or not
    not_my_comments = []
    for comment in all_comments:
        # print('comment.author =', comment.author)
        if str(comment.author) != 'SomeBottomText':
            not_my_comments.append(comment)
    # HINT:
    # checking if this code is working is a bit more complicated than in the previous tasks;
    # reddit does not directly provide the number of comments in a submission
    # that were not gerenated by your bot,
    # but you can still check this number manually by subtracting the number
    # of comments you know you've posted from the number above;
    # you can use comments that you post manually while logged into your bot to know 
    # how many comments there should be. 
    print('len(not_my_comments)=',len(not_my_comments))

    # if the length of your all_comments and not_my_comments lists are the same,
    # then that means you have not posted any comments in the current submission;
    # (your bot may have posted comments in other submissions);
    # your bot will behave differently depending on whether it's posted a comment or not
    has_not_commented = len(not_my_comments) == len(all_comments)
    print('has_not_commented=', has_not_commented)

    if has_not_commented:
        # FIXME (task 2)
        # if you have not made any comment in the thread, then post a top level comment
        #
        # HINT:
        # use the generate_comment() function to create the text,
        # and the .reply() function to post it to reddit;
        # a top level comment is created when you reply to a post instead of a message
        # pass
        text = generate_comment()
        submission.reply(text)
        print('I made a comment!')

    else:
        # FIXME (task 3): filter the not_my_comments list to also remove comments that 
        # you've already replied to
        # HINT:
        # there are many ways to accomplish this, but my solution uses two nested for loops
        # the outer for loop loops over not_my_comments,
        # and the inner for loop loops over all the replies of the current comment from the outer loop,
        # and then an if statement checks whether the comment is authored by you or not
        comments_without_replies = [] # FIX
        for comment in not_my_comments:
            for reply in comment.replies:
                if reply.author != 'SomeBottomText':
                    comments_without_replies.append(reply)
            
        # HINT:
        # this is the most difficult of the tasks,
        # and so you will have to be careful to check that this code is in fact working correctly
        print('len(comments_without_replies)=',len(comments_without_replies))

        # FIXME (task 4): randomly select a comment from the comments_without_replies list,
        # and reply to that comment
        #
        # HINT:
        # use the generate_comment() function to create the text,
        # and the .reply() function to post it to reddit;
        # these will not be top-level comments;
        # so they will not be replies to a post but replies to a message
        # pass
        r = random.choice(comments_without_replies)
        text = generate_comment()
        try:
            r.reply(text)
            print('I made a reply!')
        except praw.exceptions.APIEXCEPTION:
            print('Deleted comment - not replying')
            pass

    # FIXME (task 5): select a new submission for the next iteration;
    # your newly selected submission should be randomly selected from the 5 hottest submissions
    # pass
    submission = random.choice() #select 5 hottest submissions

    # Use this as reference:
    '''for submission in reddit.subreddit("BotTown").hot(time_filter='day', limit=5): # why top? use new, be a hero
    print('score=', submission.score, 'title=', submission.title) # can change .title to .score

    # use this link - https://praw.readthedocs.io/en/stable/index.html
    '''
    # We sleep just for 1 second at the end of the while loop.
    # This doesn't avoid rate limiting
    # (since we're not sleeping for a long period of time),
    # but it does make the program's output more readable.
    time.sleep(10) # set at 15-20 when actually running