import random

Hello = ('hello','hey','hii','hi','hai','heee','hay')

reply_Hello = ('Hello Ayushi , I Am Jarvis .',
            "Hey , What's Up ?",
            "Hey How Are You ?",
            "Hello Ayushi , Nice To Meet You Again .",
            "Of Course Ayushi , Hello .")

Name=(' hi what is your name',
        'what is your name',
        'who are you')

reply_Name=('My name is Jarvis.', 
            'jarvis.')

Beauty=('hi jarvis am i beautiful', 
            'do you think i am preety', 
                'does someone like me')

reply_Beauty=('Oh yes you are a wonderful soul.',
         'Yup you are more brighter than stars for me.',
                'Ofcourse I like you.',
                     'you are so talented.')





Bye = ('bye','exit','sleep','go')

reply_bye = ('Bye Bye Ayushi.',
            "It's Okay .",
            "It Will Be Nice To Meet You .",
            "Bye.",
            "Thanks.",
            "Okay.")

How_Are_You = ("how are you",'are you fine')

reply_how = ('I Am Fine.',
            "Excellent .",
            "Moj Ho rhi Hai .",
            "Absolutely Fine.",
            "I'm Fine.",
            "Thanks For Asking.")

nice = ('nice','good','thanks')

reply_nice = ('Thanks .',
            "Ohh , It's Okay .",
            "Thanks To You.")

Functions = ['functions','abilities','what can you do','features']

reply_Functions = ('I Can Perform Many Task Or Varieties Of Tasks , How Can I Help You ?',
            'I Can Call Your help you in your assignment, You really need me.',
            'I Can Message Your Mom That You Are Not Studing..',
            'I Can Tell Your Class Mentor That You Had Attended All The Online Classes On Insta , Facebbook etc!',
            'Let Me Ask You First , How Can I Help You ?',
            'If You Want Me To Tell My Features , Call : Print Features !')

sorry_reply = ("Sorry , That's Beyond My Abilities .",
                "Sorry , I Can't Do That .",
                "Sorry, Can you plese say it one more time",
                "Sorry , That's Above Me.")

def ChatterBot(Text):

    Text = str(Text)

    for word in Text.split():

        if word in Hello:

            reply = random.choice(reply_Hello)

            return reply

        elif word in Bye:

            reply = random.choice(reply_bye)

            return reply

        elif word in Beauty:
            reply=random.choice(reply_Beauty)
            return reply

        elif word in Name:
            reply=random.choice(reply_Name)
            return reply

        elif word in Beauty:
            reply=random.choice(reply_Beauty)
            return reply

            
        elif word in How_Are_You:

            reply_ = random.choice(reply_how)

            return reply_

        elif word in Functions:

            reply___ = random.choice(reply_Functions)

            return reply___

        else:

            return random.choice(sorry_reply)
