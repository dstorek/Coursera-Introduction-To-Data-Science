import sys
import json
import operator

def hw():
    tweet_file = open(sys.argv[1])
    hashtags = {} # initialize an empty dictionary

    for line in tweet_file:
        tweet = json.loads(line)

        if "entities" in tweet.keys() and "hashtags" in tweet["entities"]:
            if tweet['entities']['hashtags'] and tweet['entities']['hashtags'] != []:
                for word in tweet['entities']['hashtags']:
                    unicode_hashtag = word['text']
                    if not hashtags.has_key(unicode_hashtag):
                        hashtags[unicode_hashtag] = 1.00
                    else:
                        hashtags[unicode_hashtag] += 1.00

    # hashtags = {'a': 3.00, 'b': 2.00, 'c': 1.00, 'd': 4.00, 'e': 5, 'f': 6, 'g' : 7, 'h' :7, 'i':9, 'j': 10, 'z': 123.4}
    sorted_hashtags = sorted(hashtags.iteritems(), key=operator.itemgetter(1), reverse=True)

    if len(sorted_hashtags) >= 10:
        for x in range(0, 10):
            print sorted_hashtags[x][0], sorted_hashtags[x][1]

def lines(fp):
    print str(len(fp.readlines()))

def main():
    #tweet_file = open(sys.argv[1])
    #lines(tweet_file)
    hw()


if __name__ == '__main__':
    main()
