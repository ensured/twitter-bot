import tweepy as tw
from time import sleep
import json
import random
from datetime import datetime

# from playsound import playsound
from config import (
    blacklisted_hashtags_for_twitter_bot,
    blacklisted_usernames_for_twitter_bot,
    api_key,
    api_secret,
    access_token,
    access_token_secret,
    search,
    amount_of_posts_to_get,
    search_query,
)

auth = tw.OAuthHandler(api_key, api_secret)
auth.set_access_token(access_token, access_token_secret)
api = tw.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)


def fav_and_retweet():
    for tweet in tw.Cursor(
        api.search,
        q=search,
        lang="en",
    ).items(amount_of_posts_to_get):
        sleep(1)
        try:
            a = api.get_status(tweet.id, tweet_mode="extended")
            a = json.dumps(a._json)
            a = json.loads(a)

            # get full text of tweet/retweet so we can filter later
            if "…" in a["full_text"]:
                try:
                    a = a["retweeted_status"]["full_text"]
                except:
                    pass
            else:
                a = a["full_text"]

            # filter only tweets that contain 1 or more blacklisted hashtag
            hashtags = {
                hashtag
                for hashtag in blacklisted_hashtags_for_twitter_bot
                if hashtag in a
            }
            if len(hashtags) >= 1:
                print(f"🔴 {hashtags} found in @{tweet.user.screen_name}'s Tweet")
                continue
            if tweet.user.screen_name in blacklisted_usernames_for_twitter_bot:
                print(f"🔴 Blacklisted username found ({tweet.user.screen_name})")
                continue
            else:
                try:
                    tweet.favorite()
                    sleep(random.randint(1, 6))
                    tweet.retweet()
                    now = datetime.now()
                    current_time = now.strftime("%I:%M:%S%p")
                    print(
                        f"🟢 Liked & Retweeted @{tweet.user.screen_name}'s Tweet https://twitter.com/twitter/statuses/{tweet.id} at {current_time}"
                    )
                    sleep(random.randint(140, 180))
                except tw.TweepError as err:
                    print(err)
                except:
                    print("✘ Something else went wrong.")
        except tw.TweepError as e:
            print(e)


if __name__ == "__main__":
    while True:
        fav_and_retweet()
        print("sleeping 5 seconds..")
        import sys
        import time
        from os import system

        clear = lambda: system("clear")

        for i in range(random.randint(1, 10), 0, -1):
            sys.stdout.write(f"sleeping for {str(i)}")
            sys.stdout.flush()
            time.sleep(1)
            clear()
