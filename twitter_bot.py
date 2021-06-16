import tweepy as tw
from time import sleep
import os
import json
import datetime
from config import (
    blacklisted_hashtags,
    blacklisted_usernames,
    api_key,
    api_secret,
    access_token,
    access_token_secret,
)

auth = tw.OAuthHandler(api_key, api_secret)
auth.set_access_token(access_token, access_token_secret)
api = tw.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

# amount of posts to get before rerunning the function 'fav_and_retweet()'
amount_of_posts_to_get = (
    10  # larger the number the farther back the tweets you get (time wise)
)

# enter as many hashtags here as you want
search_a = "#CardanoNFT"
search_b = "#ADA"
search_c = "#Cardano"
search_d = "#CardanoCommunity"
search_e = "#CardanoFamily"
search_f = "#CNTF"


def fav_and_retweet():
    for tweet in tw.Cursor(
        api.search,
        q=f"{search_a} OR {search_b} OR {search_c} OR {search_d} OR {search_e} OR {search_f}",
        lang="en",
    ).items(amount_of_posts_to_get):
        a = api.get_status(tweet.id, tweet_mode="extended")
        # print(a.full_text)
        a = json.dumps(a._json)
        a = json.loads(a)

        # datetime stuff to make sure we aren't getting tweets from 15+ days ago (haven't got to finishing)
        # tod = datetime.datetime.now()
        # d = datetime.timedelta(days=15)
        # fifteen_days_ago = tod - d
        # if tweet.created_at > fifteen_days_ago:
        #     print(tweet.created_at)
        #     print("tweet within the last 15 days")
        # else:
        #     print(tweet.created_at)
        #     print("tweet not within the last 15 days")
        # sleep(3)

        # get full text of tweet/retweet so we can filter later
        if "…" in a["full_text"]:
            a = a["retweeted_status"]["full_text"]
            print(a)
            sleep(2)
        else:
            a = a["full_text"]
            print(a)
            sleep(2)

        # filter only tweets that contain 1 or more blacklisted hashtag
        hashtags = [hashtag for hashtag in blacklisted_hashtags if hashtag in a]
        if len(hashtags) >= 1:
            print(
                f"✘ {hashtags} found in @{tweet.user.screen_name}'s Tweet ---Skipping---"
            )
            continue
        if tweet.user.screen_name in blacklisted_usernames:
            print(
                f"✘ Blacklisted username found ({tweet.user.screen_name})\n---Skipping---"
            )
            continue
        else:
            try:
                tweet.favorite()
                tweet.retweet()
                print(f"✓ Liked & Retweeted @{tweet.user.screen_name}'s Tweet")
                sleep(180)
            except tw.TweepError as e:
                if (
                    len(hashtags) >= 1
                    or tweet.user.screen_name in blacklisted_usernames
                ):
                    continue
                print(str(e) + "\n")
            except:
                continue


if __name__ == "__main__":
    while True:
        fav_and_retweet()
        sleep(30)
