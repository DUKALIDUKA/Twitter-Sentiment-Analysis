import oauth2 as oauth
import urllib2 as urllib
import json
import sys

# See Assignment 1 instructions or README for how to get these credentials
access_token_key = "239474470-GjTzzrJ5z6TE7kvLHAlRNdq1xeqwMwzX8TyFNUMm"
access_token_secret = "b1mKFMHVJkSuh9PMGNlm8i759rhlzrxY9J89Yx6zYY"

consumer_key = "YOrbbidrPhyoSXS8IJCD0Q"
consumer_secret = "hd2oaCSneC5U2aJS8PrYskRyoYHwQGBQLzi3ADMVXo"

_debug = 0

oauth_token    = oauth.Token(key=access_token_key, secret=access_token_secret)
oauth_consumer = oauth.Consumer(key=consumer_key, secret=consumer_secret)

signature_method_hmac_sha1 = oauth.SignatureMethod_HMAC_SHA1()

http_method = "GET"


http_handler  = urllib.HTTPHandler(debuglevel=_debug)
https_handler = urllib.HTTPSHandler(debuglevel=_debug)

'''
Construct, sign, and open a twitter request
using the hard-coded credentials above.
'''
def twitterreq(url, method, parameters):
  req = oauth.Request.from_consumer_and_token(oauth_consumer,
                                             token=oauth_token,
                                             http_method=http_method,
                                             http_url=url,
                                             parameters=parameters)

  req.sign_request(signature_method_hmac_sha1, oauth_consumer, oauth_token)

  headers = req.to_header()

  if http_method == "POST":
    encoded_post_data = req.to_postdata()
  else:
    encoded_post_data = None
    url = req.to_url()

  opener = urllib.OpenerDirector()
  opener.add_handler(http_handler)
  opener.add_handler(https_handler)

  response = opener.open(url, encoded_post_data)

  return response

def fetchsamples():
  url = "https://stream.twitter.com/1/statuses/sample.json"
  parameters = [] #Is this list or a dictionary?
  response = twitterreq(url, "GET", parameters) #Difference between GET and POST
  for line in response:
    #print line.strip()
    publictweets = json.loads(line)
    twetter = ''
    tweet = ''
    favorite_count = ''
    source = ''
    user = ''
    lang = ''
    created_at = ''
    place = ''
    followers_count = ''
    statuses_count = ''
    friends_count = ''
    name = ''
    favourites_count = ''
    screen_name = ''
    notifications = ''
    time_zone = ''
    for k, v in publictweets.iteritems():
        if(str(k).encode('utf-8') == 'text'):
            tweet = v.encode("utf-8")
            #print tweet
        elif(str(k).encode('utf-8') == 'favorite_count'):
            favorite_count = v
            #print favorite_count
        elif(str(k).encode('utf-8') == 'source'):
            source = v.encode("utf-8")
            #print source
        elif(str(k).encode('utf-8') == 'user'):
            user = v #Also a dictionary
            for ku, vu in user.iteritems():
                if(str(ku).encode('utf-8') == 'followers_count'):
                    followers_count = v
                    #print followers_count
                elif(str(ku).encode('utf-8') == 'statuses_count'):
                    statuses_count = v
                    #print statuses_count
                elif(str(ku).encode('utf-8') == 'friends_count'):
                    friends_count = v
                    #print friends_count
                elif(str(ku).encode('utf-8') == 'name'):
                    name = v
                    #print name
                elif(str(ku).encode('utf-8') == 'favourites_count'):
                    favourites_count = v
                    #print favourites_count
                elif(str(ku).encode('utf-8') == 'screen_name'):
                    screen_name = v
                    #print screen_name
                elif(str(ku).encode('utf-8') == 'notifications'):
                    notifications = v
                    #print notifications
                elif(str(ku).encode('utf-8') == 'time_zone'):
                    time_zone = v
                    #print time_zone
        elif(str(k).encode('utf-8') == 'lang'):
            lang = v.encode("utf-8")
            #print lang
        elif(str(k).encode('utf-8') == 'created_at'):
            created_at = v.encode("utf-8")
            #print created_at
        elif(str(k).encode('utf-8') == 'place'):
            place = v
            #print place
    print tweet
    print '\n'

if __name__ == '__main__':
  fetchsamples()
