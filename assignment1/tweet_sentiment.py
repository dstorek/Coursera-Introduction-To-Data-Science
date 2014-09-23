import sys
import json
import re

def hw():
    afinnfile = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    scores = {} # initialize an empty dictionary
    for line in afinnfile:
      term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
      scores[term] = int(score)  # Convert the score to an integer.

    #print scores.items() # Print every (term, score) pair in the dictionary

    for line in tweet_file:
        score = 0
        tweet = json.loads(line)

        if tweet.get('text'):
            tweet_content = tweet['text'].split()
            for item in tweet_content:
                if re.match("^[A-Za-z]*$", item):
                    item = item.lower()
                    score += scores.get(item, 0)
            print score
        #else:
            #print score             # for cases when sample file contains "non-tweet" streaming messages like "delete"

def lines(fp):
    print str(len(fp.readlines()))

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    #lines(sent_file)
    #lines(tweet_file)
    hw()


if __name__ == '__main__':
    main()
