import tweepy as tw
from time import sleep
import json
from datetime import datetime
# import re
# from os.path import getsize
# from os import system, remove, path
from twitter_configs.main_config import (
    api_key,
    api_secret,
    access_token,
    access_token_secret,
    search,
    num_posts_to_get,
    like_and_retweet_replies,
    like_and_retweet_retweets,
    amount_of_mutual_followers,
)
from twitter_configs.blacklisted_hashtags_for_twitter_bot import (
    blacklisted_hashtags_for_twitter_bot,
)
from twitter_configs.blacklisted_usernames_for_twitter_bot import (
    blacklisted_usernames_for_twitter_bot,
)

auth = tw.OAuthHandler(api_key, api_secret)
auth.set_access_token(access_token, access_token_secret)
api = tw.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)


def get_amount_mutual_followers(tweet: tw.Status) -> set:
    tweet_poster_followers = []
    for follower_id in tw.Cursor(api.followers_ids, tweet.user.screen_name).items():
        tweet_poster_followers.append(follower_id)
    my_followers = []
    for follower_id in tw.Cursor(api.followers_ids, api.me().id).items():
        my_followers.append(follower_id)
    return set(tweet_poster_followers) & set(my_followers)


def fav_and_retweet():
    for tweet in tw.Cursor(
        api.search,
        q=search,
        lang="en",
    ).items(num_posts_to_get):
        try:
            sleep(1)
            tweet_json = api.get_status(tweet.id, tweet_mode="extended")
            tweet_json = json.dumps(tweet_json._json)
            tweet_json = json.loads(tweet_json)

            user = api.get_user(tweet_json["user"]["id"])
            date_now = datetime.now()
            created_at = user.created_at
            difference = date_now - created_at
            account_age = difference.days
            if account_age < 105:
                print("difference.days < 105")
                continue

            if tweet_json["in_reply_to_screen_name"] and not like_and_retweet_replies:
                print("skipping - like_and_retweet_replies is set to False")
                continue

            if "…" in tweet_json["full_text"]:
                try:
                    tweet_json = tweet_json["retweeted_status"]["full_text"]
                except:
                    tweet_json = tweet_json["full_text"]
            else:
                tweet_json = tweet_json["full_text"]

            hashtags = {
                hashtag
                for hashtag in blacklisted_hashtags_for_twitter_bot
                if hashtag in tweet_json
            }

            if (
                tweet.user.screen_name in blacklisted_usernames_for_twitter_bot
                or str(tweet._json) in blacklisted_usernames_for_twitter_bot
            ):
                print(f"🔴 Blacklisted username found : ({tweet.user.screen_name})")
                continue
            if "RT @" in str(tweet._json) and not like_and_retweet_retweets:
                print("skipping - like_and_retweet_retweets is set to false")
                continue

            elif len(hashtags) >= 1:
                # f"{hashtags} found in @{tweet.user.screen_name}'s Tweet\n"
                hashtags = " ".join(hashtags)
                print(f"🔴 {tweet.user.screen_name}: {hashtags}")
                continue

            # Check if there are enough mutual followers
            mutual_followers = get_amount_mutual_followers(tweet)
            if len(mutual_followers) < amount_of_mutual_followers:
                print(f"Not enough mutual followers: {len(mutual_followers)}")
                continue

            # Retweet and like the tweet
            api.retweet(tweet.id)
            # api.create_favorite(tweet.id)
            print(f"Retweeted and liked tweet by {tweet.user.screen_name}")
            sleep(400)
        except Exception as e:
            print(e)

if __name__ == "__main__":
    while True:
        fav_and_retweet()


