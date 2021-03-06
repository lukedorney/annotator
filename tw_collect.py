from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json
import re

"""
    Collects Tweets containing a particular emoji (or emoji set)
    Ignores tweets that are retweets, replies to keep data self-contained
    Ignores tweets with pictures as they provide additional discourse context
    outside the scope of this project.
    
"""

access_token = ''
access_secret = ''

consumer_key = ''
consumer_secret = ''


class StdOutListener(StreamListener):
    def __init__(self, output_file):
        super().__init__()
        self.output_file = output_file

    filter1 = "^[^RT].*$"
    filter2 = "^[^\"].*$"
    filter3 = "^[^@].*$"
    filter4 = "^[^\.@].*$"
    filter5 = "https"

    prog1 = re.compile(filter1)
    prog2 = re.compile(filter2)
    prog3 = re.compile(filter3)
    prog4 = re.compile(filter4)
    prog5 = re.compile(filter5)

    def on_data(self, data):
        """ collect tweets from twitter that comply with the above filters"""
        js = json.loads(data)
        if StdOutListener.prog1.match(js['text']) \
                and StdOutListener.prog2.match(js['text']) \
                and StdOutListener.prog3.match(js['text']) \
                and StdOutListener.prog4.match(js['text']) \
                and not StdOutListener.prog5.search(js['text']):
            self.output_file.write(data)
            print(data)
        return True

    def on_error(self, status):
        print(status)


if __name__ == '__main__':
    listener = StdOutListener(open("EMOTIONLESS_FACE_data.txt", "w", newline='', encoding='utf-8'))
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    stream = Stream(auth, listener)
    """name of file you want to save the json data to"""
    emotionless = [u'\U0001f611']
    """some of the top emojis seen in twitter at time of project"""
    top = [u'\U0001f602', u'\u2665', u'\u2764', u'\U0001f60d', u'\U0001f613', u'\U0001f604', u'\U0001f62d',
           u'\U0001f618', u'\U0001f495', u'\u263a']
    """
        put a corresponding emoji in the following 'track' parameter
        I just did one at a time out of convenience to myself,
        but you could put any number of characters in this parameter
    """
    stream.filter(track=['\U0001f611'], languages=['en'])
