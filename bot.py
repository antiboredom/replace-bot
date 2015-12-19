import json
import random
import replacer
from twython import Twython


with open('credentials.json', 'r') as credfile:
    auth = json.load(credfile)

twitter = Twython(
    auth['APP_KEY'],
    auth['APP_SECRET'],
    auth['ACCESS_TOKEN'],
    auth['ACCESS_TOKEN_SECRET']
)


def find_and_replace(search_phrase, replace_phrase, dryrun=False):

    results = twitter.search(q=search_phrase)
    tweets = results['statuses']

    texts = []

    for tweet in tweets:
        text = tweet['text'].encode('utf-8')
        new_text = replacer.replace(text, search_phrase, replace_phrase)
        if new_text != text:
            # sometimes, randomly, include the original tweeters name
            if random.random() > 0.5:
                new_text = '. @' + tweet['user']['screen_name'].encode('utf-8') + ' ' + new_text
            if len(new_text) <= 140:
                texts.append({'txt': new_text, 'id': tweet['id']})

    to_tweet = random.choice(texts)

    if dryrun is False:
        twitter.update_status(
            status=to_tweet['txt'],
            in_reply_to_status_id=to_tweet['id']
        )

    return to_tweet['txt']


if __name__ == '__main__':
    import sys
    print find_and_replace(sys.argv[1], sys.argv[2])
