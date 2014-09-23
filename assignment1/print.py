import urllib
import json

response = urllib.urlopen("https://api.twitter.com/1.1/search/tweets.json?q=microsoft")
print json.load(response)

