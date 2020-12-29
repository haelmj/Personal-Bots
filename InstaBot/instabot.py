from instapy import InstaPy
from instapy import smart_run
import os

# get os 
INSTA_USER = os.environ.get('INSTA_USER')
INSTA_PASS = os.environ.get('INSTA_PASS')

emoji_references = { "heart": ":heart_eyes:", "massage": ":man-getting-massage::skin-tone-5:", "sweat": ":sweat_smile:", "wave": ":wave::skin-tone-5:"}
filter_tags = ['naked', 'nsfw', 'mature', 'ebony']
comments = [f'Awesome post!!!{emoji_references["heart"]}',
            f"""Hey guys, I'm an instabot created by this user. 
            I normally don't like barging in {emoji_references['sweat']} but if you'd like to learn how to create your own chatbot
            then follow me as I will be posting a YouTube link done by my creator{emoji_references['massage']}""",
            f"Hi there {emoji_references['wave']}, I'm testing out this instabot in python. I apologize for dropping in like this. If you'd like to see a guide on how to create your own bot then please follow my Tech account(link in bio)"]

class IBot():
    def __init__(self):
        self.session = InstaPy(username=INSTA_USER, password=INSTA_PASS, headless_browser=True)
    
    def startsession(self):
        with smart_run(self.session):
            """Activity Flow"""
            self.session.like_by_tags(['python3', 'javascript', 'coding', 'python'], amount=10)
            self.session.set_comments(comments)
            self.session.set_do_comment(True, percentage=70)
            self.session.set_dont_like(filter_tags)

IBot().startsession()
