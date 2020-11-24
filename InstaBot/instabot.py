from instapy import InstaPy
from instapy import smart_run
import os

INSTA_USER = os.environ.get('INSTA_USER')
INSTA_PASS = os.environ.get('INSTA_PASS')

class IBot():
    def __init__(self):
        self.session = InstaPy(username=INSTA_USER, password=INSTA_PASS)
    
    def startsession(self):
        with smart_run(self.session):
            """Activity Flow"""
            self.session.like_by_tags(['python3', 'javascript'], amount=40)
