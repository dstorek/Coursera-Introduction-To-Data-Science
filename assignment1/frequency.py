import sys
import json
import re

def hw():
    tweet_file = open(sys.argv[1])
    word_count = {} # initialize an empty dictionary

    for line in tweet_file:
        tweet = json.loads(line)

        if tweet.get('text'):
            tweet_content = tweet['text'].split()
            for word in tweet_content:
                if re.match("^[A-Za-z]*$", word):
                    word = word.lower()

                    if not word_count.has_key(word):
                        word_count[word] = 1.00
                    else:
                        word_count[word] += 1.00

    for word in word_count:
       float_value = word_count[word]
       print word, float_value

def lines(fp):
    print str(len(fp.readlines()))

def main():
    #tweet_file = open(sys.argv[1])
    #lines(tweet_file)
    hw()


if __name__ == '__main__':
    main()
