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

    tweet_sentiments = {}
    word_sentiments = {}
    new_words = {}

    for line in tweet_file:
        score = 0
        tweet = json.loads(line)

        current_dict = {}

        if tweet.get('text'):
            tweet_content = tweet['text'].split()
            for item in tweet_content:
                if re.match("^[A-Za-z]*$", item):
                    item = item.lower()
                    score += scores.get(item, 0)
            tweet_sentiments[line] = score
            # print "tweet_sentiments: " + str(tweet_sentiments[line])

            for word in tweet_content:
                if re.match("^[A-Za-z]*$", word):
                    word = word.lower()

                    if not scores.has_key(word):
                        if not word_sentiments.has_key(word):
                            # print word + ' : does not exists'
                            word_sentiments[word] = [0]

                        if tweet_sentiments[line] != 0 and not current_dict.has_key(word):
                            # word_sentiments[word].append(tweet_sentiments[line])
                            word_sentiments[word][0] += tweet_sentiments[line]
                            current_dict[word] = 0
                        # print word_sentiments

            # print score
        #else:
            #print score             # for cases when sample file contains "non-tweet" streaming messages like "delete"

    # print "WORD SENTIMENTS: " + str(word_sentiments)

    for word in  word_sentiments:
        if word_sentiments[word][0] == 0:
            new_words[word] = 0.00
        elif word_sentiments[word][0] > 0:
            new_words[word] = 1.00
        else:
            new_words[word] = -1.00

    for word in new_words:
        value = new_words[word]
        print word, value


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
