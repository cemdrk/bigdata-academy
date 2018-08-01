from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''


class TwitterListener(StreamListener):
    def on_data(self, data):
        with open('output.txt', 'a') as outfile:
            outfile.write(data)
        return True

    def on_error(self, status):
        print(status)
        return False


if __name__ == '__main__':
    listener = TwitterListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, listener)
    stream.filter(track=['Dolar'], languages=['tr'])
